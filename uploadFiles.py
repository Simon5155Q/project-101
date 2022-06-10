import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BFRrJ2Ck45CdT8CeynT9KC8BUqGFxezGjp_tu2kgPSHGMFwkSISlyMWJp1Awmdn4-Gsjj27QKSvjgdaMX1FlRzKe9SmPYPV6FEtHofGLWBdjYsFQlO4-A0b9XgGESO2sGb3BAqcxEo_t"
    transferData = TransferData(access_token) 

    file_from = input("Enter your path: ") 
    file_to = input("Enter your path: ")
    transferData.upload_file(file_from, file_to)
    print("The file has been transfered")

main()

