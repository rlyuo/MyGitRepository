import unittest
import requests
import json
import xlrd

class MyCookie(unittest.TestCase):

    def test_get_all_job_names(self):
           file = 'JieKou.xlsx'
           wb = xlrd.open_workbook(filename=file)  # 打开文件
           sheet1 = wb.sheet_by_name('post请求')  # 通过名字获取表格
           #url = 'https://bankplus-s-beta.jd.com/fe/beta-16/fw/trade/page'
           #cookies='qd_uid=K90XAAJ3-4B4TXOYZJGE6XRJY6G2P;qd_fs=1586930230474;__jda=122270672.15869302380211437379971.1586930238.1586930238.1586930238.1;__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1586930238022;mba_muid=15869302380211437379971;shshshfp=890cc9cb48c525011468b4788a67de69;shshshfpa=dbe13377-1511-9a54-41c5-9dae4c2c9a6d-1586930238;shshshfpb=ysQ7RSBpi8raOtXBVVf1GBQ%3D%3D;3AB9D23F7A4B3C9B=RGDJIU7IWLWCNWFTS4YHA5HORFRKGUZEITDDJSNCI673RIA3K2RXIWYAVKGEUXFMUM6ZVIGXDPR2MPPAOPMUPXMGOE;TrackerID=fE2ul9N-5VJYB2IV6YwWSpQFRq4KGBvnpr3AggTPMY8xaDkLahhXpHdTUv6rcipcb8fdbOQrYZGJWaB3dK_lpcayAaKfHlC7CFlLGEDEnFH9LADVxrSwxAFd52k9voll;pt_key=AAJelqJZADC0btMuuk-bIcRRmtL4qXL9AmCvzJtqN1NCdjPHy6Idec7tt-sgFBfGudjeSD4yDjU;pt_pin=jd_77ed323b7fef4;pt_token=lxplwjdi;pwdt_id=jd_77ed323b7fef4;qd_ad=-%7C-%7Cdirect%7C-%7C0;qd_sq=4;qd_ls=1587029617473;qd_ts=1587047277378;qd_sid=K90XAAJ3-4B4TXOYZJGE6XRJY6G2P-4'
           url=sheet1.cell(1,0).value
           cookies=sheet1.cell(1,1).value
           headers= {'Cookie':cookies,'Content-Type': 'application/json'}
           postdata = {'curPage':1,'pageSize':10,'channelId':'hmccb','portal':'OTHER','container': 'WEB','uuid':'9987142462638875','imei': '9987142462638875','deviceId':'9987142462638875'}
           r=requests.post(url,data=json.dumps(postdata),headers=headers,verify=False)
           json.load(r.text)
           print(r.text)


if __name__ == '__main__':
	coo = MyCookie()
	coo.test_get_all_job_names()
