{
  "targets": [
    {
      "target_name": "kv-wiredtiger",
	  "include_dirs" : [
        "<!(node -e \"require('nan')\")",
        "<!(node -e \"require('kv-common')\")",
        "deps/include"
      ],
      "dependencies": [
        "<(module_root_dir)/deps/wiredtiger/wiredtiger.gyp:wiredtiger"
      ],
      "sources": [
        "src/main.cpp"
      ],
      "conditions": [
        [
          "OS == 'win'", {
            "defines": [
              "_HAS_EXCEPTIONS=0"
            ],
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeTypeInfo': 'false',
                'EnableFunctionLevelLinking': 'true',
                'ExceptionHandling': '2',
                'DisableSpecificWarnings': [ '4267' ]
              }
            }
          }
        ],
        [
          "OS=='linux'", {
            "cflags_cc": [ "-std=c++0x" ],
            "ldflags": ["-static-libstdc++"]
          }
        ],
        [
          'OS == "mac"', {
            'xcode_settings': {
              'MACOSX_DEPLOYMENT_TARGET': '10.7',
              'OTHER_CPLUSPLUSFLAGS': [
                  '-std=c++11' ,
                  '-stdlib=libc++'
              ]
            }
          }
        ]
      ]
    }
  ]
}