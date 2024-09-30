# coding:utf-8
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines

# def rename():
#     name_list= get_filename()
#     for name in name_list:
#         new_name = "kenwood/" + name.split("/")[-1]
#         print(new_name)


def pull_image():
    name_list= get_filename()
    
    for name in name_list:
         subprocess.call("docker login -u 763742347@qq.com -p xujinjun830513 crpi-4t784y1dkvir02m5.cn-hangzhou.personal.cr.aliyuncs.com", shell=True)
        if 'sha256' in name:
            print(name)
            sha256_name = name.split("@")
            #new_name = sha256_name[0].split("/")[-1]
            new_name = sha256_name[0]
            tag = sha256_name[-1].split(":")[-1][0:6]
            image = "crpi-4t784y1dkvir02m5.cn-hangzhou.personal.cr.aliyuncs.com/xujinjunimages/" + new_name + ":"+ tag
            cmd = "docker tag {0}   {1}".format(name, image)
            subprocess.call("docker pull {}".format(name), shell=True)
            print("docker pull {}".format(name))
            subprocess.run(["docker", "tag", name, image])
            subprocess.call("docker push {}".format(image), shell=True)
            print("docker push {}".format(image))
        else:
            #new_name = "crpi-4t784y1dkvir02m5.cn-hangzhou.personal.cr.aliyuncs.com/xujinjunimages/" + name.split("/")[-1]
            new_name = "crpi-4t784y1dkvir02m5.cn-hangzhou.personal.cr.aliyuncs.com/xujinjunimages/" + name
            cmd = "docker tag {0}   {1}".format(name, new_name)
            subprocess.call("docker pull {}".format(name), shell=True)
            print("docker pull {}".format(name))
            subprocess.run(["docker", "tag", name, new_name])
           
            subprocess.call("docker push {}".format(new_name), shell=True)

            print("docker push {}".format(new_name))
        
if __name__ == "__main__":
    pull_image()
