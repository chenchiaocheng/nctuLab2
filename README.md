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
>> `mininet> [server] iperf -s -u -i 1 > "��X��}"(�Ҧp: ./out/result) &`
>> `mininet> [client] iperf -c "server IP" -u -i 1`
> * Show the screenshot of using iPerf command in Mininet
>>![](https://i.imgur.com/L3x7WhY.png)

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail
>> * `addSwitch("switch name")` : �K�[�@��switch��ݾ�
>> * `addHost("host name")` : �K�[�@��host��ݾ�
>> * `addLink("node", "node", bw = ?, delay = '?ms', loss = ?)` : �K�[���V�����ݾ�A�ó]�w�W�e(Mbits)�B����(ms)�B�l��(%)
>> * `start()` : �}�l�B�����
>> * `pingAll()` : ���թҦ��`�I�������s�q��
>> * `dumpNodeConnections()` : �C�X�ݾ뤺�Ҧ��`�I��connection�T��
>> * `CLI()` : Mininet CLI�Ұ�
>> * `setLogLevel('info')` : �]�wMininet�q�{��output level

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail
>> * h4 iperf -s : ���h4�@��server�ݡA�Hserver�Ҧ��Ұ� 
>> * -u : �ϥ�UDP(�w�]��TCP)
>> * -i 1 : ���i�ɶ����j1��
>> * h2 iperf -c 10.0.4 : ���h2�@��client�ݡA�åB�s��IP��}10.0.0.4���A�Ⱥ�
>> 
>>> `mininet> h4 iperf -s -u -i 1 > ./out/result &`
>>> `mininet> h2 iperf -c 10.0.0.4 -u -i 1`

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**
> * **Step1. Join the lab on GitHub**
>> * �[�Jlab
https://classroom.github.com/a/K8gaizQG 
>> * �i�JGitHub group https://github.com/nctucn
> * **Step2. Login to your contaier using SSH**
>> * �}��Pietty�A�ÿ�JIP address : 140.113.195.69��port : 16021
>> 
>>> ![](https://i.imgur.com/dKmam6e.png)
>> * �n�J->Login: root  Passward: cn2018
> * **Step3. Clone your GitHub repository**
>> * ���Ƨ��qGitHub�W��U��
>> `git clone https://github.com/nctucn/lab2-chenchiaocheng.git`
> * **Step4. Run Mininet for testing**
>> * �B��Mininet 
>> `sudo mn`
>> * �p�G�X�{: You may wish to try "service openvswitch-switch start".�h�NOpen vSwitch�ҰʡA��J:
>> `sudo service openvswitch-switch start`
>> `sudo mn`
2. **Example of Mininet**
> * **���� example.py**
>> * ���i��/lab2-chenchiaocheng/src/���|��
>> * �N�ɮ��ܦ������ɡA�A����
>> `sudo chm +x example.py`
>> `sudo ./example.py`
>> * �p�G�X�{: File exists�A��J�U�����O�M�����e�����
>> `sudo mn -c`
3. **Topology Generator**
> * **Step1. View the topology you should generate**
>> * ���n���ͪ�topology�A�Ǹ��᤭�X%3->16021%3=1�A�n���ͪ�topology�ptopo1.png
> * **Step2. Generate the topology via Mininet**
>> * �Ѧ�example.py�g�Xtopology.py�A�Q�ΤW�����쪺Mininet API�ӧ����Atopology.py�����Ѧ������C�@�B�b���ƻ�

4. **Measurement**
> * **Use iPerf commands to measure the topology you built**
>> * ������topology.py�A�T�{connection
>> `sudo chm +x topology.py`
>> `sudo ./topology.py`
>> * ���ۿ�J
>> `mininet> h4 iperf -s -u -i 1 > ./out/result &`
>> `mininet> h2 iperf -c 10.0.0.4 -u -i 1`
>> * �b./lab2-chenchiaocheng/src/out/result �i�H��쵲�G->�o��the rate of packet loss : 51%
>> * topo1.png �o�쪺��������51%~58%
---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
	* [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
	* [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
	* [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
	* [GitHub/OSE-Lab - ���x�p��ϥ� Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
	* [�Ұs�ͪ��O�ƥ� �V Mininet ���O](https://blog.laszlo.tw/?p=81)
	* [Hwchiu Learning Note �V ���⥴�y�� mininet ����](https://hwchiu.com/setup-mininet-like-environment.html)
	* [���e������� �V Mininet ���O����](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
	* [Mininet �ǲ߫��n](https://www.sdnlab.com/11495.html)
	* [SDN �����t�Τ� Mininet �P API �Ը�](https://hk.saowen.com/a/14d7c14b01c541dd2e53991ea67f1c5ca0d6406bdcb07a9d44065b3d4a37f6d7)
	* [Mininet �챴�ƾڤ��ߺ���](https://www.jianshu.com/p/b74f3f5cbe34)
	* [SDN(�n��w�q����)������-Mininet](https://zhuanlan.zhihu.com/p/30935141)
* **Python**
	* [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
	* [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
	* [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
	* [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
	* [Vim Tutorial �V Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
	* [������ Linux �p�е� �V �ĤE���Bvim �{���s�边](http://linux.vbird.org/linux_basic/0310vi.php)
	* [iperf �V �έp jitter �H�� packet loss](http://benjr.tw/3030)
	* [�Q�� iperf ���պ����į�](https://cms.35g.tw/coding/%E5%88%A9%E7%94%A8-iperf-%E6%B8%AC%E8%A9%A6%E7%B6%B2%E8%B7%AF%E6%95%88%E8%83%BD/)
	* [Markdown �y�k����](https://markdown.tw/#p)
	* [Markdown ����](https://kingofamani.gitbooks.io/git-teach/content/chapter_6_gitbook/markdown.html?q=)
	* [�p�󷾳q��ơG���q�żаO���y��-�ϥ� Markdown ��U�g�@��r�ԭz](https://medium.com/datainpoint/communicating-md-e53a08e6652f)

---
## Contributors
> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [Chen Chiao Cheng](https://github.com/chenchiaocheng)
* [David Lu](https://github.com/yungshenglu)

---
## License
																							
GNU GENERAL PUBLIC LICENSE Version 3
