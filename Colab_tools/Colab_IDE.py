class Colab_IDE:
  def __init__(self,IDE,tunnelling,name,password,mount_GD):
    self.IDE = IDE
    self.tunnelling = tunnelling
    self.name = name
    self.password = password
    self.mount_GD = mount_GD
    self.web_port = 8787

    # add Linux user
    self.create_user()

    # mount Google Drive
    self.Google_Drive()

  def create_user(self):
    os.system("useradd -m -s /bin/bash" + " " + str(self.name))
    os.system("echo '" + str(self.name) + ":" + str(self.password) + "' | chpasswd")
    os.system("usermod -G sudo" + " " + str(self.name))
  
  def Google_Drive(self):
    if self.mount_GD:
      from google.colab import drive
      drive.mount('/content/drive')

  # install web IDE

  def Install_Rstudio_server(self,web_port=None,verbose=True):

    # check param
    if (web_port is None):
      web_port = self.web_port

    # install
    char_cmd = "bash /content/IDE_on_Colab/web_IDE/Install_Rstudio_server.sh" + " " + str(web_port)
    Running_log = subprocess.run(char_cmd,capture_output=True,shell=True,check=True,universal_newlines=True)
    if verbose:
      print("stdout:\n" + str(Running_log.stdout).replace('\\n','\n'))
      print("stderr:\n" + str(Running_log.stderr).replace('\\n','\n'))

  def Install_code_server(self,web_port=None,web_password=None,verbose=True):

    # check param
    if (web_port is None):
      web_port = self.web_port
    if (web_password is None):
      web_password = self.password

    # install
    os.system("apt install expect")
    char_cmd = "expect /content/IDE_on_Colab/web_IDE/Install_code_server.exp" + " " + str(self.name) + " " + str(self.password) + " " + str(web_port) + " " + str(web_password)
    Running_log = subprocess.run(char_cmd,capture_output=True,shell=True,check=True,universal_newlines=True)
    char_cmd = "expect /content/IDE_on_Colab/web_IDE/Run_code_server.exp" + " " + str(self.name)
    os.system(char_cmd)
    if verbose:
      print("stdout:\n" + str(Running_log.stdout).replace('\\n','\n'))
      print("stderr:\n" + str(Running_log.stderr).replace('\\n','\n'))

  # run tunnelling
  def Run_localtunnel(self,web_port=None):

    # check param
    if (web_port is None):
      web_port = self.web_port

    # install
    char_cmd = "bash /content/IDE_on_Colab/tunnelling/Run_localtunnel.sh" + " " + str(web_port)
    os.system(char_cmd)

  def Run_ngrok(self,web_port=None):

    # check param
    if (web_port is None):
      web_port = self.web_port

    # input token
    ngrok_token = input("Input your ngrok token:")

    # install
    char_cmd = "bash /content/IDE_on_Colab/tunnelling/Run_ngrok.sh" + " " + str(ngrok_token) + " " + str(web_port)
    os.system(char_cmd)
