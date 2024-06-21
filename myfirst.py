import requests
url= "https://www.amazon.com/s?k=amazon+to+amazon&adgrpid=143351077583&hvadid=642553445208&hvdev=c&hvlocphy=9061363&hvnetw=g&hvqmt=b&hvrand=3165012072434928904&hvtargid=kwd-302052016531&hydadcr=22338_13333071&tag=hydglogoo-20&ref=pd_sl_35e5oxzz0v_b"
r = requests.get(url)
print(r.status_code)