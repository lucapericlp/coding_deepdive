[![HitCount](http://hits.dwyl.io/lucaperic.lp/lucaperic.lp/.svg)](http://hits.dwyl.io/lucaperic.lp/lucaperic.lp/)
# coding_deepdive
Repo to attain a deeper understanding of data structures and algorithm design.

Structure of repo is divided into main topics which are then divided into easy, medium, hard. These are found by using the [leetcode-cli](https://github.com/skygragon/leetcode-cli) by using query utility such as:

```bash
#questions containing array within title 
leetcode list -q e array 

#questions in array tag within leetcode and marked easy 
leetcode list -t array -q e 
```

And then using the command below to generate the source file for the desired question and print instructions 

```bash
leetcode show 1 -g -l python3
```
