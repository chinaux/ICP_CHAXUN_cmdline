ICP_CHAXUN_cmdline
==================

search available icp 
环境： 
  win7
  python 2.7.6
  配置环境变量path
    
文件：
  start_icp.bat
  icp.py
  
  
使用方法：
  1.把 ICP_CHAXUN 文件夹复制到任意位置
  2.修改start_icp.bat 中的 初始icp 和 后续查询条数
    如下 查询以09091971 开始的后续 4 个icp
    python icp.py 09091971 4
    pause
  3.查询结果存入同目录下的 gotICP.csv 文件
  
  
注意：目前只支持查询 京备 ICP 号
