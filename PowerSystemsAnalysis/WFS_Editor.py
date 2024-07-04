import os
class WorkData():

    def __init__(self, save_path, path=None, lista=None):

        if path:

            files = os.listdir(path)
            with open(save_path, 'w') as f:
                for line in files:
                    f.write(line + '\n')
                    # print(line)

        elif lista:

            with open(save_path, 'w') as f:
              for line in lista:
                  f.write(line + '\n')
                #   print(line)