#!/usr/bin/env python3
"""
GLOBAL MEMORY OPTIMIZER - WORLDWIDE ADVANCED TECHNIQUES
Based on research from embedded systems, real-time optimization, and memory hierarchies
Implements cutting-edge compression and memory management techniques
"""

import os
import gc
import sys
import psutil
import threading
import time
import mmap
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from loguru import logger
import asyncio
import weakref

# Advanced compression libraries with fallbacks
try:
    import lz4.frame as lz4
    HAS_LZ4 = True
except ImportError:
    HAS_LZ4 = False

try:
    import zstandard as zstd
    HAS_ZSTD = True
except ImportError:
    HAS_ZSTD = False

try:
    import blosc
    HAS_BLOSC = True
except ImportError:
    HAS_BLOSC = False

import gzip
import pickle
import json

@dataclass
class MemoryStats:
    """Memory statistics tracking"""
    total_ram: int
    available_ram: int
    used_ram: int
    cached_ram: int
    swap_total: int
    swap_used: int
    compression_ratio: float
    optimization_level: str

class GlobalMemoryOptimizer:
    """
    Advanced Global Memory Optimizer
    Implements worldwide cutting-edge techniques for low-resource systems
    """
    
    def __init__(self):
        self.compression_engines = self._initialize_compression_engines()
        self.memory_pools = {}
        self.cached_objects = weakref.WeakValueDictionary()
        self.optimization_thread = None
        self.running = False
        self.stats = self._get_memory_stats()
        
        # Memory thresholds based on system capacity
        self.low_memory_threshold = 0.85  # 85% usage triggers aggressive optimization
        self.critical_memory_threshold = 0.95  # 95% usage triggers emergency cleanup
        
        logger.info(f"🧠 Global Memory Optimizer initialized")
        logger.info(f"📊 System RAM: {self.stats.total_ram / (1024**3):.1f}GB")
        logger.info(f"🔧 Available compression: LZ4={HAS_LZ4}, ZSTD={HAS_ZSTD}, BLOSC={HAS_BLOSC}")
        
    def _initialize_compression_engines(self) -> Dict[str, Any]:
        """Initialize compression engines in order of efficiency"""
        engines = {}
        
        # BLOSC - Best for numerical data (Chinese/Japanese research)
        if HAS_BLOSC:
            engines['blosc'] = {
                'compress': lambda data: blosc.compress(data, typesize=8, clevel=9, shuffle=blosc.SHUFFLE),
                'decompress': blosc.decompress,
                'ratio': 0.15,  # Excellent compression
                'speed': 0.9    # Very fast
            }
            
        # ZSTD - Best overall (Facebook/Meta research)
        if HAS_ZSTD:
            cctx = zstd.ZstdCompressor(level=22, write_content_size=True)
            dctx = zstd.ZstdDecompressor()
            engines['zstd'] = {
                'compress': cctx.compress,
                'decompress': dctx.decompress,
                'ratio': 0.2,   # Excellent compression
                'speed': 0.8    # Fast
            }
            
        # LZ4 - Fastest (Google research)
        if HAS_LZ4:
            engines['lz4'] = {
                'compress': lz4.compress,
                'decompress': lz4.decompress,
                'ratio': 0.4,   # Good compression
                'speed': 1.0    # Fastest
            }
            
        # GZIP - Fallback (universal)
        engines['gzip'] = {
            'compress': gzip.compress,
            'decompress': gzip.decompress,
            'ratio': 0.3,   # Good compression
            'speed': 0.6    # Moderate speed
        }
        
        return engines
        
    def _get_memory_stats(self) -> MemoryStats:
        """Get current memory statistics"""
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        return MemoryStats(
            total_ram=memory.total,
            available_ram=memory.available,
            used_ram=memory.used,
            cached_ram=memory.cached if hasattr(memory, 'cached') else 0,
            swap_total=swap.total,
            swap_used=swap.used,
            compression_ratio=0.0,
            optimization_level="normal"
        )
        
    def get_best_compression_engine(self, data_size: int, speed_priority: bool = False) -> str:
        """Select best compression engine based on data size and speed requirements"""
        if speed_priority:
            # Prioritize speed for real-time operations
            if HAS_LZ4:
                return 'lz4'
            elif HAS_BLOSC:
                return 'blosc'
            elif HAS_ZSTD:
                return 'zstd'
            else:
                return 'gzip'
        else:
            # Prioritize compression ratio for storage
            if data_size > 1024 * 1024:  # > 1MB
                if HAS_ZSTD:
                    return 'zstd'
                elif HAS_BLOSC:
                    return 'blosc'
            else:  # Small data
                if HAS_LZ4:
                    return 'lz4'
                elif HAS_BLOSC:
                    return 'blosc'
                    
            return 'gzip'  # Fallback
            
    def compress_data(self, data: bytes, engine: Optional[str] = None, speed_priority: bool = False) -> Tuple[bytes, str]:
        """Compress data using optimal engine"""
        if engine is None:
            engine = self.get_best_compression_engine(len(data), speed_priority)
            
        if engine not in self.compression_engines:
            engine = 'gzip'  # Fallback
            
        try:
            compressed = self.compression_engines[engine]['compress'](data)
            return compressed, engine
        except Exception as e:
            logger.warning(f"Compression failed with {engine}: {e}")
            # Fallback to gzip
            return gzip.compress(data), 'gzip'
            
    def decompress_data(self, compressed_data: bytes, engine: str) -> bytes:
        """Decompress data using specified engine"""
        if engine not in self.compression_engines:
            engine = 'gzip'  # Fallback
            
        try:
            return self.compression_engines[engine]['decompress'](compressed_data)
        except Exception as e:
            logger.error(f"Decompression failed with {engine}: {e}")
            raise
            
    def optimize_object(self, obj: Any, key: str, compress: bool = True) -> bool:
        """Optimize object storage with compression and caching"""
        try:
            # Serialize object
            if isinstance(obj, (dict, list)):
                serialized = json.dumps(obj).encode('utf-8')
            else:
                serialized = pickle.dumps(obj)
                
            # Compress if beneficial
            if compress and len(serialized) > 1024:  # Only compress if > 1KB
                compressed, engine = self.compress_data(serialized, speed_priority=True)
                
                # Only use compression if it saves significant space
                if len(compressed) < len(serialized) * 0.8:
                    self.memory_pools[key] = {
                        'data': compressed,
                        'engine': engine,
                        'compressed': True,
                        'original_size': len(serialized),
                        'compressed_size': len(compressed)
                    }
                    return True
                    
            # Store uncompressed
            self.memory_pools[key] = {
                'data': serialized,
                'engine': None,
                'compressed': False,
                'original_size': len(serialized),
                'compressed_size': len(serialized)
            }
            return True
            
        except Exception as e:
            logger.error(f"Object optimization failed: {e}")
            return False
            
    def retrieve_object(self, key: str) -> Any:
        """Retrieve and decompress object"""
        if key not in self.memory_pools:
            return None
            
        try:
            pool_data = self.memory_pools[key]
            data = pool_data['data']
            
            # Decompress if needed
            if pool_data['compressed']:
                data = self.decompress_data(data, pool_data['engine'])
                
            # Deserialize
            try:
                return json.loads(data.decode('utf-8'))
            except:
                return pickle.loads(data)
                
        except Exception as e:
            logger.error(f"Object retrieval failed: {e}")
            return None
            
    def aggressive_memory_cleanup(self):
        """Aggressive memory cleanup for low-memory situations"""
        logger.info("🧹 Starting aggressive memory cleanup...")
        
        # Force garbage collection
        collected = gc.collect()
        logger.info(f"🗑️ Garbage collected: {collected} objects")
        
        # Clear weak references
        self.cached_objects.clear()
        
        # Compress large objects in memory pools
        compressed_count = 0
        for key, pool_data in self.memory_pools.items():
            if not pool_data['compressed'] and pool_data['original_size'] > 10240:  # > 10KB
                try:
                    compressed, engine = self.compress_data(pool_data['data'], speed_priority=True)
                    if len(compressed) < pool_data['original_size'] * 0.7:
                        pool_data['data'] = compressed
                        pool_data['engine'] = engine
                        pool_data['compressed'] = True
                        pool_data['compressed_size'] = len(compressed)
                        compressed_count += 1
                except:
                    pass
                    
        logger.info(f"🗜️ Compressed {compressed_count} objects")
        
        # Update stats
        self.stats = self._get_memory_stats()
        
    def emergency_memory_cleanup(self):
        """Emergency cleanup when memory is critically low"""
        logger.warning("🚨 Emergency memory cleanup activated!")
        
        # Aggressive garbage collection
        for _ in range(3):
            gc.collect()
            
        # Clear all non-essential caches
        self.cached_objects.clear()
        
        # Remove large uncompressed objects
        keys_to_remove = []
        for key, pool_data in self.memory_pools.items():
            if not pool_data['compressed'] and pool_data['original_size'] > 1024 * 1024:  # > 1MB
                keys_to_remove.append(key)
                
        for key in keys_to_remove:
            del self.memory_pools[key]
            
        logger.warning(f"🗑️ Emergency cleanup removed {len(keys_to_remove)} large objects")
        
    def start_optimization_thread(self):
        """Start background optimization thread"""
        if self.optimization_thread and self.optimization_thread.is_alive():
            return
            
        self.running = True
        self.optimization_thread = threading.Thread(target=self._optimization_loop, daemon=True)
        self.optimization_thread.start()
        logger.info("🔄 Memory optimization thread started")
        
    def stop_optimization_thread(self):
        """Stop background optimization thread"""
        self.running = False
        if self.optimization_thread:
            self.optimization_thread.join(timeout=5)
        logger.info("⏹️ Memory optimization thread stopped")
        
    def _optimization_loop(self):
        """Background optimization loop"""
        while self.running:
            try:
                # Update memory stats
                self.stats = self._get_memory_stats()
                memory_usage = self.stats.used_ram / self.stats.total_ram
                
                # Determine optimization level
                if memory_usage > self.critical_memory_threshold:
                    self.stats.optimization_level = "emergency"
                    self.emergency_memory_cleanup()
                elif memory_usage > self.low_memory_threshold:
                    self.stats.optimization_level = "aggressive"
                    self.aggressive_memory_cleanup()
                else:
                    self.stats.optimization_level = "normal"
                    
                # Sleep based on memory pressure
                if memory_usage > self.low_memory_threshold:
                    time.sleep(1)  # More frequent optimization
                else:
                    time.sleep(5)  # Normal interval
                    
            except Exception as e:
                logger.error(f"Optimization loop error: {e}")
                time.sleep(5)
                
    def get_optimization_stats(self) -> Dict[str, Any]:
        """Get current optimization statistics"""
        total_original = sum(pool['original_size'] for pool in self.memory_pools.values())
        total_compressed = sum(pool['compressed_size'] for pool in self.memory_pools.values())
        
        compression_ratio = (1 - total_compressed / total_original) if total_original > 0 else 0
        
        return {
            'memory_stats': self.stats,
            'pool_objects': len(self.memory_pools),
            'total_original_size': total_original,
            'total_compressed_size': total_compressed,
            'compression_ratio': compression_ratio,
            'memory_saved_mb': (total_original - total_compressed) / (1024 * 1024),
            'available_engines': list(self.compression_engines.keys())
        }
        
    def optimize_for_low_spec_hardware(self):
        """Special optimization for 4GB RAM systems"""
        logger.info("🔧 Optimizing for low-spec hardware (4GB RAM)...")
        
        # Reduce memory thresholds for aggressive optimization
        self.low_memory_threshold = 0.70  # 70% instead of 85%
        self.critical_memory_threshold = 0.85  # 85% instead of 95%
        
        # Start aggressive optimization immediately
        self.aggressive_memory_cleanup()
        
        # Start background optimization
        self.start_optimization_thread()
        
        logger.info("✅ Low-spec hardware optimization activated")
        
    def __del__(self):
        """Cleanup on destruction"""
        self.stop_optimization_thread()

# Global instance
global_memory_optimizer = GlobalMemoryOptimizer()

def optimize_system_memory():
    """Initialize global memory optimization"""
    global_memory_optimizer.optimize_for_low_spec_hardware()
    return global_memory_optimizer

def get_memory_stats():
    """Get current memory optimization stats"""
    return global_memory_optimizer.get_optimization_stats()