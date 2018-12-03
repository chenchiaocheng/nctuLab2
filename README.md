# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> TODO: 
> * Describe how to execute your program
>> 1. Change the directory into /lab-chenchiaocheng/src/:
>> 2. Change to the executable mode of topology.py
>> `sudo chmod +x topology.py`
>> 3. Run topology.py
>> `sudo ./topology.py`
>> 4. Use iPerf commands to get the rate of packet loss
>> `mininet> [server] iperf -s -u -i 1 > "輸出位址"(例如: ./out/result) &`
>> `mininet> [client] iperf -c "server IP" -u -i 1`
> * Show the screenshot of using iPerf command in Mininet
>>![](https://i.imgur.com/L3x7WhY.png)

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail
>> * `addSwitch("switch name")` : 添加一個switch到拓樸
>> * `addHost("host name")` : 添加一個host到拓樸
>> * `addLink("node", "node", bw = ?, delay = '?ms', loss = ?)` : 添加雙向鏈路到拓樸，並設定頻寬(Mbits)、延遲(ms)、損失(%)
>> * `start()` : 開始運行網路
>> * `pingAll()` : 測試所有節點之間的連通性
>> * `dumpNodeConnections()` : 列出拓樸內所有節點的connection訊息
>> * `CLI()` : Mininet CLI啟動
>> * `setLogLevel('info')` : 設定Mininet默認的output level

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail
>> * h4 iperf -s : 選擇h4作為server端，以server模式啟動 
>> * -u : 使用UDP(預設為TCP)
>> * -i 1 : 報告時間間隔1秒
>> * h2 iperf -c 10.0.4 : 選擇h2作為client端，並且連接IP位址10.0.0.4的服務端
>> 
>>> `mininet> h4 iperf -s -u -i 1 > ./out/result &`
>>> `mininet> h2 iperf -c 10.0.0.4 -u -i 1`

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
> * **Step1. Join the lab on GitHub**
>> * 加入lab
https://classroom.github.com/a/K8gaizQG 
>> * 進入GitHub group https://github.com/nctucn
> * **Step2. Login to your contaier using SSH**
>> * 開啟Pietty，並輸入IP address : 140.113.195.69跟port : 16021
>> 
>>> ![](https://i.imgur.com/dKmam6e.png)
>> * 登入->Login: root  Passward: cn2018
> * **Step3. Clone your GitHub repository**
>> * 把資料夾從GitHub上抓下來
>> `git clone https://github.com/nctucn/lab2-chenchiaocheng.git`
> * **Step4. Run Mininet for testing**
>> * 運行Mininet 
>> `sudo mn`
>> * 如果出現: You may wish to try "service openvswitch-switch start".則將Open vSwitch啟動，輸入:
>> `sudo service openvswitch-switch start`
>> `sudo mn`
2. **Example of Mininet**
> * **執行 example.py**
>> * 先進到/lab2-chenchiaocheng/src/路徑中
>> * 將檔案變成執行檔，再執行
>> `sudo chm +x example.py`
>> `sudo ./example.py`
>> * 如果出現: File exists，輸入下面指令清除先前的資料
>> `sudo mn -c`
3. **Topology Generator**
> * **Step1. View the topology you should generate**
>> * 找到要產生的topology，學號後五碼%3->16021%3=1，要產生的topology如topo1.png
> * **Step2. Generate the topology via Mininet**
>> * 參考example.py寫出topology.py，利用上面提到的Mininet API來完成，topology.py的註解有解釋每一步在做甚麼

4. **Measurement**
> * **Use iPerf commands to measure the topology you built**
>> * 先執行topology.py，確認connection
>> `sudo chm +x topology.py`
>> `sudo ./topology.py`
>> * 接著輸入
>> `mininet> h4 iperf -s -u -i 1 > ./out/result &`
>> `mininet> h2 iperf -c 10.0.0.4 -u -i 1`
>> * 在./lab2-chenchiaocheng/src/out/result 可以找到結果->得到the rate of packet loss : 51%
>> * topo1.png 得到的值應介於51%~58%
---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
	* [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
	* [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
	* [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
	* [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
	* [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
	* [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
	* [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
	* [Mininet 學習指南](https://www.sdnlab.com/11495.html)
	* [SDN 網絡系統之 Mininet 與 API 詳解](https://hk.saowen.com/a/14d7c14b01c541dd2e53991ea67f1c5ca0d6406bdcb07a9d44065b3d4a37f6d7)
	* [Mininet 初探數據中心網路](https://www.jianshu.com/p/b74f3f5cbe34)
	* [SDN(軟體定義網路)初體驗-Mininet](https://zhuanlan.zhihu.com/p/30935141)
* **Python**
	* [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
	* [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
	* [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
	* [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
	* [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
	* [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)
	* [iperf – 統計 jitter 以及 packet loss](http://benjr.tw/3030)
	* [利用 iperf 測試網路效能](https://cms.35g.tw/coding/%E5%88%A9%E7%94%A8-iperf-%E6%B8%AC%E8%A9%A6%E7%B6%B2%E8%B7%AF%E6%95%88%E8%83%BD/)
	* [Markdown 語法說明](https://markdown.tw/#p)
	* [Markdown 風格](https://kingofamani.gitbooks.io/git-teach/content/chapter_6_gitbook/markdown.html?q=)
	* [如何溝通資料：輕量級標記式語言-使用 Markdown 協助寫作文字敘述](https://medium.com/datainpoint/communicating-md-e53a08e6652f)

---
## Contributors
> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [Chen Chiao Cheng](https://github.com/chenchiaocheng)
* [David Lu](https://github.com/yungshenglu)

---
## License
																							
GNU GENERAL PUBLIC LICENSE Version 3
