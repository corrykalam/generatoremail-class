import requests
class generatorEmail:
    def getStr(self,string,start,end, index=1):
        try:
            str = string.split(start)
            str = str[index].split(end)
            return str[0]
        except:
            return False

    def getVerificationCode(self,email, fromMail, start, end):
        try:
            email = email.split("@")
            cookies = {
                'surl': '%s/%s'%(email[1],email[0])
            }
            post = requests.get("https://generator.email/", cookies=cookies)
            if fromMail in post.text:
                code = self.getStr(post.text, start, end)
                return code
            else:
                return False
        except Exception as e:
            print(e)
    
    def getMailBox(self, email):
        email = email.split("@")
        cookies = {
            'surl': '%s/%s'%(email[1],email[0])
        }
        post = requests.get("https://generator.email/", cookies=cookies)
        return post.text
        
    def getRandomEmail(self):
        post = requests.get("https://generator.email").text
        domainEmail = self.getStr(post, '"email_ch_text">', '<')
        return domainEmail