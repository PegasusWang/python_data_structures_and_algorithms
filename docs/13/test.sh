

#!/usr/bin/env bash

# pip install when-changed, 监控文件变动并且文件修改之后自动执行 pytest 单测，方便我们边修改边跑测试
 when-changed -v -r -1 -s ./    "py.test -s $1"

