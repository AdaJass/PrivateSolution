import asyncio

@asyncio.coroutine
def slow_operation(future):
    future.set_result('Future is done!')
    yield from asyncio.sleep(5)
    future.set_result('Future are done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print(future.result())
loop.close()

'''
SINAGLOBAL=4101766048397.4727.1457666572383;
wb_publish_vip_5896005318=1; wb_publish_fist100_5896005318=1;
myuid=5896005318; un=18701115105; wvr=6;
SUS=SID-5896005318-1461303485-XD-lxhiw-8248eb95a1ea059989157511021c7852; 
SUE=es%3Dda43682d92b6238d8da2959f377b4785%26ev%3Dv1%26es2%3De27bf0106c3828ee6aacd375aa9d462c%26rs0%3DdJAJgm3BYAJjASzazmbw5QaLXNJuvLOE9FwMHZVyCw3UXXGSAUWuRWtKqvvZzUbendac7MdSeEWRMsyMwYUT5zM2oSzaRzZmB85XCHa6WU1JgzQOARTGRbsRXLKinMECyZ1f5zw5w1cCIGO%252FmUwLfmVDMz6Be2W6IsjbkFE1%252F1s%253D%26rv%3D0; 
SUP=cv%3D1%26bt%3D1461303485%26et%3D1461389885%26d%3Dc909%26i%3D7852%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D5896005318%26name%3D18701115105%26nick%3D%25E8%25A6%2583%25E6%2580%259D%25E9%2592%25A7%26fmp%3D%26lcp%3D; SUB=_2A256HcjtDeRxGeNG4lQR8CvPyjSIHXVZar0lrDV8PUNbvtAPLW_tkW9LHetq-9ssiGT-jOfbX2lCuJaQQinqZw..;
SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Ze6bCc.Vlk69OWLrmQHS25JpX5KMt; SUHB=0rr72a7ItUyln7; ALF=1492839485; SSOLoginState=1461303485; _s_tentry=login.sina.com.cn; Apache=1193117033934.6787.1461303510721; ULV=1461303510809:44:33:8:1193117033934.6787.1461303510721:1461292579294; TC-Page-G0=6fdca7ba258605061f331acb73120318;
TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e;
WBtopGlobal_register_version=60539f809b40ed0d; 
ULOGIN_IMG=14613036063579; 
TC-V5-G0=8518b479055542524f4cf5907e498469; 
UOR=www.csdn.net,widget.weibo.com,login.sina.com.cn
'''

'''
 SINAGLOBAL=4101766048397.4727.1457666572383;
 wb_publish_vip_5896005318=1; 
 wb_publish_fist100_5896005318=1; 
 un=18701115105; 
 SUHB=0rr72a7ItUyln7; 
 _s_tentry=login.sina.com.cn; 
 Apache=1193117033934.6787.1461303510721; 
 ULV=1461303510809:44:33:8:1193117033934.6787.1461303510721:1461292579294; 
 TC-Page-G0=6fdca7ba258605061f331acb73120318; 
 TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; 
 ULOGIN_IMG=14613036063579; 
 TC-V5-G0=8518b479055542524f4cf5907e498469; 
 WBtopGlobal_register_version=60539f809b40ed0d; 
 myuid=5896005318; 
 SUB=_2AkMgRTWpdcPhrAZZkf4VzG7hbYVMywDzudfwMUvdFyYzHBt_7j5nqSVo8kZ_Xd6h2GvmYbQyCDc7WvmhJ2jQnDWxnlcV; 
 SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5Ze6bCc.Vlk69OWLrmQHS25JpVF02RS05peK2feK5f; 
 login_sid_t=149d2fe7d8b2022db80d2b54c679d00f; 
 UOR=www.csdn.net,widget.weibo.com,login.sina.com.cn
 '''