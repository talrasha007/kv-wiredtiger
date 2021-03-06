{
  "targets": [
    {
      "target_name": "wiredtiger",
      "type": "static_library",
      "standalone_static_library": 1,
      "variables": {
        "wt_version": "2.5.2"
      },
      "dependencies": [
        "../snappy/snappy.gyp:snappy"
      ],
      "include_dirs": [
        "../include",
        "wiredtiger-<(wt_version)/src/include"
      ],
      "defines": [
        "HAVE_BUILTIN_EXTENSION_SNAPPY=1",
        "HAVE_LIBSNAPPY=1"
      ],
      "sources": [
        "wiredtiger-<(wt_version)/src/async/async_api.c",
        "wiredtiger-<(wt_version)/src/async/async_op.c",
        "wiredtiger-<(wt_version)/src/async/async_worker.c",
        "wiredtiger-<(wt_version)/src/block/block_addr.c",
        "wiredtiger-<(wt_version)/src/block/block_ckpt.c",
        "wiredtiger-<(wt_version)/src/block/block_compact.c",
        "wiredtiger-<(wt_version)/src/block/block_ext.c",
        "wiredtiger-<(wt_version)/src/block/block_map.c",
        "wiredtiger-<(wt_version)/src/block/block_mgr.c",
        "wiredtiger-<(wt_version)/src/block/block_open.c",
        "wiredtiger-<(wt_version)/src/block/block_read.c",
        "wiredtiger-<(wt_version)/src/block/block_session.c",
        "wiredtiger-<(wt_version)/src/block/block_slvg.c",
        "wiredtiger-<(wt_version)/src/block/block_vrfy.c",
        "wiredtiger-<(wt_version)/src/block/block_write.c",
        "wiredtiger-<(wt_version)/src/bloom/bloom.c",
        "wiredtiger-<(wt_version)/src/btree/bt_compact.c",
        "wiredtiger-<(wt_version)/src/btree/bt_curnext.c",
        "wiredtiger-<(wt_version)/src/btree/bt_curprev.c",
        "wiredtiger-<(wt_version)/src/btree/bt_cursor.c",
        "wiredtiger-<(wt_version)/src/btree/bt_debug.c",
        "wiredtiger-<(wt_version)/src/btree/bt_delete.c",
        "wiredtiger-<(wt_version)/src/btree/bt_discard.c",
        "wiredtiger-<(wt_version)/src/btree/bt_handle.c",
        "wiredtiger-<(wt_version)/src/btree/bt_huffman.c",
        "wiredtiger-<(wt_version)/src/btree/bt_io.c",
        "wiredtiger-<(wt_version)/src/btree/bt_misc.c",
        "wiredtiger-<(wt_version)/src/btree/bt_ovfl.c",
        "wiredtiger-<(wt_version)/src/btree/bt_page.c",
        "wiredtiger-<(wt_version)/src/btree/bt_read.c",
        "wiredtiger-<(wt_version)/src/btree/bt_ret.c",
        "wiredtiger-<(wt_version)/src/btree/bt_slvg.c",
        "wiredtiger-<(wt_version)/src/btree/bt_split.c",
        "wiredtiger-<(wt_version)/src/btree/bt_stat.c",
        "wiredtiger-<(wt_version)/src/btree/bt_sync.c",
        "wiredtiger-<(wt_version)/src/btree/bt_upgrade.c",
        "wiredtiger-<(wt_version)/src/btree/bt_vrfy.c",
        "wiredtiger-<(wt_version)/src/btree/bt_vrfy_dsk.c",
        "wiredtiger-<(wt_version)/src/btree/bt_walk.c",
        "wiredtiger-<(wt_version)/src/btree/col_modify.c",
        "wiredtiger-<(wt_version)/src/btree/col_srch.c",
        "wiredtiger-<(wt_version)/src/btree/row_key.c",
        "wiredtiger-<(wt_version)/src/btree/row_modify.c",
        "wiredtiger-<(wt_version)/src/btree/row_srch.c",
        "wiredtiger-<(wt_version)/src/config/config.c",
        "wiredtiger-<(wt_version)/src/config/config_api.c",
        "wiredtiger-<(wt_version)/src/config/config_check.c",
        "wiredtiger-<(wt_version)/src/config/config_collapse.c",
        "wiredtiger-<(wt_version)/src/config/config_concat.c",
        "wiredtiger-<(wt_version)/src/config/config_def.c",
        "wiredtiger-<(wt_version)/src/config/config_ext.c",
        "wiredtiger-<(wt_version)/src/config/config_upgrade.c",
        "wiredtiger-<(wt_version)/src/conn/api_strerror.c",
        "wiredtiger-<(wt_version)/src/conn/api_version.c",
        "wiredtiger-<(wt_version)/src/conn/conn_api.c",
        "wiredtiger-<(wt_version)/src/conn/conn_cache.c",
        "wiredtiger-<(wt_version)/src/conn/conn_cache_pool.c",
        "wiredtiger-<(wt_version)/src/conn/conn_ckpt.c",
        "wiredtiger-<(wt_version)/src/conn/conn_dhandle.c",
        "wiredtiger-<(wt_version)/src/conn/conn_handle.c",
        "wiredtiger-<(wt_version)/src/conn/conn_log.c",
        "wiredtiger-<(wt_version)/src/conn/conn_open.c",
        "wiredtiger-<(wt_version)/src/conn/conn_stat.c",
        "wiredtiger-<(wt_version)/src/conn/conn_sweep.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_backup.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_bulk.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_config.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_ds.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_dump.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_file.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_index.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_json.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_log.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_metadata.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_stat.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_std.c",
        "wiredtiger-<(wt_version)/src/cursor/cur_table.c",
        "wiredtiger-<(wt_version)/src/evict/evict_file.c",
        "wiredtiger-<(wt_version)/src/evict/evict_lru.c",
        "wiredtiger-<(wt_version)/src/evict/evict_page.c",
        "wiredtiger-<(wt_version)/src/log/log.c",
        "wiredtiger-<(wt_version)/src/log/log_auto.c",
        "wiredtiger-<(wt_version)/src/log/log_slot.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_cursor.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_manager.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_merge.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_meta.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_stat.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_tree.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_work_unit.c",
        "wiredtiger-<(wt_version)/src/lsm/lsm_worker.c",
        "wiredtiger-<(wt_version)/src/meta/meta_apply.c",
        "wiredtiger-<(wt_version)/src/meta/meta_ckpt.c",
        "wiredtiger-<(wt_version)/src/meta/meta_ext.c",
        "wiredtiger-<(wt_version)/src/meta/meta_table.c",
        "wiredtiger-<(wt_version)/src/meta/meta_track.c",
        "wiredtiger-<(wt_version)/src/meta/meta_turtle.c",
        "wiredtiger-<(wt_version)/src/os_posix/os_abort.c",
        "wiredtiger-<(wt_version)/src/os_posix/os_alloc.c",
        "wiredtiger-<(wt_version)/src/os_posix/os_getline.c",
        "wiredtiger-<(wt_version)/src/os_posix/os_getopt.c",
        "wiredtiger-<(wt_version)/src/os_posix/os_mtx_rw.c",
        "wiredtiger-<(wt_version)/src/os_posix/os_strtouq.c",
        "wiredtiger-<(wt_version)/src/packing/pack_api.c",
        "wiredtiger-<(wt_version)/src/packing/pack_impl.c",
        "wiredtiger-<(wt_version)/src/packing/pack_stream.c",
        "wiredtiger-<(wt_version)/src/reconcile/rec_track.c",
        "wiredtiger-<(wt_version)/src/reconcile/rec_write.c",
        "wiredtiger-<(wt_version)/src/schema/schema_create.c",
        "wiredtiger-<(wt_version)/src/schema/schema_drop.c",
        "wiredtiger-<(wt_version)/src/schema/schema_list.c",
        "wiredtiger-<(wt_version)/src/schema/schema_open.c",
        "wiredtiger-<(wt_version)/src/schema/schema_plan.c",
        "wiredtiger-<(wt_version)/src/schema/schema_project.c",
        "wiredtiger-<(wt_version)/src/schema/schema_rename.c",
        "wiredtiger-<(wt_version)/src/schema/schema_stat.c",
        "wiredtiger-<(wt_version)/src/schema/schema_truncate.c",
        "wiredtiger-<(wt_version)/src/schema/schema_util.c",
        "wiredtiger-<(wt_version)/src/schema/schema_worker.c",
        "wiredtiger-<(wt_version)/src/session/session_api.c",
        "wiredtiger-<(wt_version)/src/session/session_compact.c",
        "wiredtiger-<(wt_version)/src/session/session_dhandle.c",
        "wiredtiger-<(wt_version)/src/session/session_salvage.c",
        "wiredtiger-<(wt_version)/src/support/cksum.c",
        "wiredtiger-<(wt_version)/src/support/err.c",
        "wiredtiger-<(wt_version)/src/support/filename.c",
        "wiredtiger-<(wt_version)/src/support/global.c",
        "wiredtiger-<(wt_version)/src/support/hash_city.c",
        "wiredtiger-<(wt_version)/src/support/hash_fnv.c",
        "wiredtiger-<(wt_version)/src/support/hazard.c",
        "wiredtiger-<(wt_version)/src/support/hex.c",
        "wiredtiger-<(wt_version)/src/support/huffman.c",
        "wiredtiger-<(wt_version)/src/support/mutex.c",
        "wiredtiger-<(wt_version)/src/support/pow.c",
        "wiredtiger-<(wt_version)/src/support/rand.c",
        "wiredtiger-<(wt_version)/src/support/scratch.c",
        "wiredtiger-<(wt_version)/src/support/stat.c",
        "wiredtiger-<(wt_version)/src/txn/txn.c",
        "wiredtiger-<(wt_version)/src/txn/txn_ckpt.c",
        "wiredtiger-<(wt_version)/src/txn/txn_ext.c",
        "wiredtiger-<(wt_version)/src/txn/txn_log.c",
        "wiredtiger-<(wt_version)/src/txn/txn_recover.c",
        "wiredtiger-<(wt_version)/ext/compressors/snappy/snappy_compress.c"
      ],
      "conditions": [
        [
          "OS == 'win'", {
            "include_dirs": [
              "wiredtiger-<(wt_version)/build_win"
            ],
            "sources": [
              "wiredtiger-<(wt_version)/src/os_win/os_dir.c",
              "wiredtiger-<(wt_version)/src/os_win/os_dlopen.c",
              "wiredtiger-<(wt_version)/src/os_win/os_errno.c",
              "wiredtiger-<(wt_version)/src/os_win/os_exist.c",
              "wiredtiger-<(wt_version)/src/os_win/os_fallocate.c",
              "wiredtiger-<(wt_version)/src/os_win/os_filesize.c",
              "wiredtiger-<(wt_version)/src/os_win/os_flock.c",
              "wiredtiger-<(wt_version)/src/os_win/os_fsync.c",
              "wiredtiger-<(wt_version)/src/os_win/os_ftruncate.c",
              "wiredtiger-<(wt_version)/src/os_win/os_getenv.c",
              "wiredtiger-<(wt_version)/src/os_win/os_map.c",
              "wiredtiger-<(wt_version)/src/os_win/os_mtx_cond.c",
              "wiredtiger-<(wt_version)/src/os_win/os_once.c",
              "wiredtiger-<(wt_version)/src/os_win/os_open.c",
              "wiredtiger-<(wt_version)/src/os_win/os_path.c",
              "wiredtiger-<(wt_version)/src/os_win/os_priv.c",
              "wiredtiger-<(wt_version)/src/os_win/os_remove.c",
              "wiredtiger-<(wt_version)/src/os_win/os_rename.c",
              "wiredtiger-<(wt_version)/src/os_win/os_rw.c",
              "wiredtiger-<(wt_version)/src/os_win/os_sleep.c",
              "wiredtiger-<(wt_version)/src/os_win/os_snprintf.c",
              "wiredtiger-<(wt_version)/src/os_win/os_thread.c",
              "wiredtiger-<(wt_version)/src/os_win/os_time.c",
              "wiredtiger-<(wt_version)/src/os_win/os_vsnprintf.c",
              "wiredtiger-<(wt_version)/src/os_win/os_yield.c"
            ],
            "msvs_settings": {
              "VCCLCompilerTool": {
                "RuntimeTypeInfo": "false",
                "EnableFunctionLevelLinking": "true",
                "ExceptionHandling": "2",
                "DisableSpecificWarnings": [ "4024", "4047", "4133", "4244", "4267", "4090" ]
              }
            }
          }
        ],
        [
          "OS != 'win'", {
            "cflags": [
              "-Wno-implicit-function-declaration",
              "-Wno-uninitialized"
            ],
            "include_dirs": [
              "wiredtiger-<(wt_version)/build_posix"
            ],
            "sources": [
              "wiredtiger-<(wt_version)/src/os_posix/os_dir.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_dlopen.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_errno.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_exist.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_fallocate.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_filesize.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_flock.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_fsync.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_ftruncate.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_getenv.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_map.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_mtx_cond.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_once.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_open.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_path.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_priv.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_remove.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_rename.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_rw.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_sleep.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_thread.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_time.c",
              "wiredtiger-<(wt_version)/src/os_posix/os_yield.c"
            ]
          }
        ],
        [
          "OS == 'linux'", {
            "defines": [
              "HAVE_CLOCK_GETTIME=1",
              "HAVE_FALLOCATE=1",
              "HAVE_POSIX_FADVISE=1"
            ]
          }
        ],
        [
          "OS == 'mac'", {
            "xcode_settings": {
              "WARNING_CFLAGS": [
                "-Wno-implicit-function-declaration"
              ]
            }
          }
        ]
      ]
    }
  ]
}
