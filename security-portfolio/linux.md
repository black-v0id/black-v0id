# Project: Managing File Permissions with Linux

## Backgound 
<details>
  You are a security professional at a large organization. You mainly work with their research team. Part of your job is to ensure users on this team are authorized with the appropriate permissions. This helps keep the system secure. 

Your task is to examine existing permissions on the file system. You’ll need to determine if the permissions match the authorization that should be given. If they do not match, you’ll need to modify the permissions to authorize the appropriate users and remove any unauthorized access.
</details>

## Report
## Existing Permissions
![image](https://github.com/black-v0id/black-v0id/assets/16123062/c0f9c501-df69-449b-b2ed-607fc595d27c)

Within the research projects directory there are 4 projects, 1 hidden project, and 1 sub directory for drafts. 

Group for this directory is the `research_team`. 

`project_k.txt` : user= read, write; group= read, write; other= read,write

`project_m.txt` : user= read, write; group= read; others= -

`project_r.txt` : user= read, write; group= read, write; other= read

`project_t.txt` : user= read, write; group= read, write; other= read

`.project_x.txt` : user= read, write; group= write; other= -

`drafts` : user= read, write, execute; group= execute, write; other= -


**🤔 How do we know this?**

Linux permissions can be deciphered as such

```
-rw-rw-rw- 1 researcher2 research_team   46 Jun 30 18:35 project_k.txt
|[-][-][-]   [---------] [-----------]      [----------] [-----------]
| |  |  |        |            |                  |            + ---------> File Name
| |  |  |        |            |                  + ----------------------> Date permissions were listed
| |  |  |        |            + -----------------------------------------> Group
| |  |  |        + ------------------------------------------------------> Owner
| |  |  + ---------------------------------------------------------------> Others Permissions
| |  + ------------------------------------------------------------------> Group Permissions
| + ---------------------------------------------------------------------> User Whom is File Owner Permissions
+ -----------------------------------------------------------------------> File Type
```

The first section within the printed line is a 10 digit permission string for the file or directory. The first digit signifies what type of file it is (- for file, d for directory etc.), next the string is broken into triplets where the first first group of three denotes the permissions for the user that is the owner (`u`), the second group of three denotes the permissions for the group (`g`) and the last group of three denote the permissions for others (`o`) - aka anyone on the internet that can find that file. 

Permissions that can be assigned are read (`r`), write (`w`) and execute (`e`). If owner, group or other has that permission it is designated by the shorthand (`r`,`w`,`x`) and if it does not have that permission it is designated by a `-` character.  

Thus we can conclude that for `project_k`:
- the owner has `rw-` permissions aka read and write but not execute.
- the group has `rw-` permissions aka read and write but not execute.
- the others has `rw-` permissions aka read and write but not execute.


## Update Permissions
The organization does not allow other to have write access to any files.

![image](https://github.com/black-v0id/black-v0id/assets/16123062/a3dd12d5-05b5-4776-9396-f2990ad3ed25)

`chmod` is the linux command to change permissions on a file or directory. After specifying whom is getting modified (`u` user that is file owner, `g` for group, `o` for other) you can add permissions `+`, remove permissions `-` or re-write them as specified `=`. 

💡 Additionally, this has me thinking about what uses of `find` or `grep` I could write up to make this task simpler. Something like ```find ./projects -regex `[_m|_k|_t]` | chmod o=-```. Looking at that, I might need a more robust script that has a varible for the current file and feeds it to chmod then loops through the remaining files. 

## Private Project Lockdown
The research team has archived .project_x.txt, which is why it’s a hidden file. This file should not have write permissions for anyone, but the user and group should be able to read the file. Use a Linux command to assign .project_x.txt the appropriate authorization.

![image](https://github.com/black-v0id/black-v0id/assets/16123062/266c9176-ebcd-4d0f-a8f9-6f46dc3ca412)

⏪ Looking back, I struggled with multiple changes and have realized it was because I was using a space after the comma and getting an error. If I redid this and took a new screenshot I would shorten the code to `chmod u=r,g=r .project_x.txt`


## Directory Lockdown
The files and directories in the projects directory belong to the researcher2 user. Only researcher2 should be allowed to access the drafts directory and its contents. Use a Linux command to modify the permissions accordingly.

![image](https://github.com/black-v0id/black-v0id/assets/16123062/7f63f6c6-40e9-4e2d-a34c-ce3c0222dce7)


## Summary
I was able to apply skills in order to change the permissions on files based on security requirements. I used common linux commands such as `ls` and `chmod` to complete this task as well as deeper knowledge of the syntax used to decipher exisiting permissions and update to new requirements. 

