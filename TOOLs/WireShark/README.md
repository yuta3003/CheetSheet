# WireShark
- [Display Filter](#display-filter)
- [Capture Filter](#capture-filter)

## Display Filter
キャプチャ可能なパケットを全て取得し、必要なパケットをフィルタリングする方法

|フィルタ|説明|
|---|---|
|eth.src==98:e0:d9:xx:xx:xx|送信元MACアドレスが一致するものを表示|
|eth.dst==98:e0:d9:xx:xx:xx|宛先MACアドレスが一致するものを表示|
|ip.addr==192.168.1.1| 送信元または宛先IPが192.168.1.1|
|ip.src==192.168.1.1| 送信元IPが192.168.1.1|
|ip.dst==192.168.1.1| 宛先IPが192.168.1.1|
|tcp.port==80| 送信元または宛先TCPポート番号が80|
|tcp.srcport==80| 送信元TCPポートが80|
|tcp.dwtport==80| 宛先TCPポートが80|
|tcp.flags.syn(ack, fin, reset) == 1|SYN(ACK, FIN, RST)パケットを表示|
|udp.port==53| 送信元または宛先ポートが53|
|dns.qry.name==ドメイン名|ドメイン名からIPアドレスを解決するメッセージを表示| 
|プロトコル(tcp, udp, icmp, http, arp...)|プロトコルのフレームを表示|
|tcp.analysis.retransmission| TCP の再送パケットを表示|

## Capture Filter
特定のパケットのみをキャプチャするフィルタリング方法
