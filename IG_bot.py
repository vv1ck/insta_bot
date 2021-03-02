import requests , re , time , random 
from instabot import Bot
r = requests.session()
b = Bot

print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
██╗ ██████╗       By JOKER @t.uo    V2
██║██╔════╝     
██║██║  ███╗    ██████    ██████  ████████     
██║██║   ██║    ██   ██  ██    ██    ██    
██║╚██████╔╝    ██████   ██    ██    ██  
╚═╝ ╚═════╝     ██   ██  ██    ██    ██    
    AUTO -->>   ██████    ██████     ██   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


joker = input('>> [1] Follow   [2] Likes   [3] comment \n->>  ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')

urlLG = 'https://www.instagram.com/accounts/login/ajax/'
headerLG = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'content-length': '269',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'ig_did=CBE027FC-62A2-4383-85BB-63843B14C94F; ig_nrcb=1; mid=X85qiQALAAFugGOZjugz_zBUZQHx; datr=SD8HYG1W7e-ghmx_vRH1TB7V; fbm_124024574287414=base_domain=.instagram.com; shbid=3563; shbts=1612115664.6497803; rur=VLL; csrftoken=y3yTqqHa0mjqe3ytTy9IBMXw23Z5TT3G',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua-mobile': '?1',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
	'x-csrftoken': 'y3yTqqHa0mjqe3ytTy9IBMXw23Z5TT3G',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': 'hmac.AR2kUU6QD4ZMYLZ-anFcEb7SWiyQTfkx3NQ_KuXrhuCHqUhr',
	'x-instagram-ajax': '7a3a3e64fa87',
	'x-requested-with': 'XMLHttpRequest'}

if joker == '1':
	tr = input('Enter the account name : ')
	sle = int(input('Enter sleep [ 3 / 7 ] : '))
	print(' ')
	def folo():
		time.sleep(1)
		si = j.cookies['sessionid']
		url_id = 'https://www.instagram.com/{}/?__a=1'.format(tr)
		req_id = r.get(url_id).json()
		user_id = str(req_id['logging_page_id'])
		iid = user_id.split('_')[1]
		url = 'https://www.instagram.com/web/friendships/{}/follow/'.format(iid)
		
		headers2 = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+si,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/themostflorya/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
			'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
			'x-ig-app-id': iid,
			'x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu',
			'x-instagram-ajax': '95bfef5dd816',
			'x-requested-with': 'XMLHttpRequest'}
		
		g = r.post(url, headers=headers2).text
		if '"status":"ok"':
			print(f'\n[Ok] Done Follow ID({iid})')
		else:
			print('\n[ERROR] >> I did not add him')
		
	for x in open('user.txt','r').read().splitlines():
		user = x.split(":")[0]
		pess = x.split(":")[1]
		
		data1 = {
			'username': f'{user}',
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pess}'}
		
		j = r.post(urlLG, headers=headerLG, data=data1)
		if '"authenticated":true' in j.text:
			print(f"Done Login {user}")
			folo()
		elif "checkpoint_required" in j.text:
			print(f'\n[stop] >> Account Secure {user}!')
		else:
			print(f'Error Login {user} ')

#.   مالك شغل

elif joker == '2':
	urPO = input("Enter url post :")
	sle = int(input('Enter sleep [ 3 / 7 ] : '))
	def like():
		time.sleep(1)
		idd = b.get_media_id_from_link(self='',link=urPO)
		si = j.cookies['sessionid']
		LIK = 'https://www.instagram.com/web/likes/{}/like/'.format(idd)
		
		headers2 = {
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+si,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/p/CLmJsGXHGbB/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
			'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
			'x-ig-app-id': idd,
			'x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0MktDQ',
			'x-instagram-ajax': '95bfef5dd816',
			'x-requested-with': 'XMLHttpRequest'}
		
		g = r.post(LIK,headers=headers2).text
		
		if '"status":"ok"' in g:
			print(f'\n[OK] >> Done likes ID post({idd})')
			
		else:
			print('\n[ERROR] >> I did not put likes')
			
	for x in open('user.txt','r').read().splitlines():
		user = x.split(":")[0]
		pess = x.split(":")[1]
		
		data1 = {
			'username': f'{user}',
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pess}'}
		
		j = r.post(urlLG, headers=headerLG, data=data1)
		if '"authenticated":true' in j.text:
			print(f"Done Login {user}")
			like()
		elif "checkpoint_required" in j.text:
			print(f'\n[stop] >> Account Secure {user}!')
		else:
			print(f'Error Login {user} ')
			
#.   مالك شغل
if joker == '3':
	urlPO = input("Enter url post :")
	com1 = input('Enter comment : ')
	sle = int(input('Enter sleep [ 3 / 7 ] : '))
	
	def com():
		time.sleep(1)
		com = com1
		idd = b.get_media_id_from_link(self='',link=urlPO)
		si = j.cookies['sessionid']
		url = 'https://www.instagram.com/web/comments/{}/add/'.format(idd)
		
		headers3 = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '38',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+si,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/p/CLi-c3dnVmX/?igshid=11qxb01iil7kl',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
			'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
			'x-ig-app-id': idd,
			'x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu',
			'x-instagram-ajax': '95bfef5dd816',
			'x-requested-with': 'XMLHttpRequest'}
		data3 = {
			'comment_text': f'{com}',
			'replied_to_comment_id':''}
		
		g=r.post(url, headers=headers3,data=data3).text
		if '"status":"ok"' in g:
			print(f'[Ok] Done cooment ID({idd})')
		else:
			print('\n[ERROR] >> I did not put comment')
	
	
	for x in open('user.txt','r').read().splitlines():
		user = x.split(":")[0]
		pess = x.split(":")[1]
		
		
		data1 = {
			'username': f'{user}',
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pess}'}
		
		j = r.post(urlLG, headers=headerLG, data=data1)
		if '"authenticated":true' in j.text:
			print(f"Done Login {user}")
			com()
		elif "checkpoint_required" in j.text:
			print(f'\n[stop] >> Account Secure {user}!')
		else:
			print(f'Error Login {user} ! ')
				
else:
	print('   Please enter the correct number !')
	print('           [ 1 - 2 - 3 ]')
