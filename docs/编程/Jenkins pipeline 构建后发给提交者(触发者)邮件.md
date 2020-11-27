每次Jenkins走pipeline自动构建时，我需要等待构建完成，上到测试环境后再通知测试或者项目去跟近，    
最开始想用机器人，后面发现发邮件很简单，我也有邮件弹窗提示，所以让jenkins做完后发个做完的邮件给我。    
    
![](..\images\7485616-82b560786e888659.jpg)    
    
    
    
Jenkinsfile中增加两段代码:    
    
> 1. 在stage该在的地方添加下列代码    
```    
        stage("get GIT_COMMIT_NAME/GIT_COMMIT_EMAIL") {    
            agent any    
            steps {    
                checkout scm    
                script {    
                    // Git committer name    
                    env.git_commit_name = sh (script: "git --no-pager show -s --format='%an' $GIT_COMMIT",returnStdout: true).trim()    
                    echo "Git committer name: ${GIT_COMMIT_NAME}"    
                    // Git committer email    
                    env.git_commit_email = sh (script: "git --no-pager show -s --format='%ae' $GIT_COMMIT",returnStdout: true).trim()    
                    echo "Git committer email: ${GIT_COMMIT_EMAIL}"    
                }    
            }    
```    
    
    
> 2. 在文件最后一个花括号前面增加下列代码    
```    
    post {    
        success {    
            script {    
                mail to: "${env.git_commit_email}",    
                subject: "[Jenkins] SUCCESSFUL: ${env.appName} [${env.BUILD_NUMBER}]",    
                body: """SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'    
分支: ${env.BRANCH_NAME}    
JOB_NAME: ${env.JOB_NAME}    
提交人: ${env.git_commit_name}    
构建次数：${env.BUILD_NUMBER}    
console output：${env.BUILD_URL}    
                """    
            }    
        }    
        failure {    
             script {    
                mail to: "${env.git_commit_email}",    
                subject: "[Jenkins] FAILURE: ${env.appName} [${env.BUILD_NUMBER}]",    
                body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'    
分支: ${env.BRANCH_NAME}    
JOB_NAME: ${env.JOB_NAME}    
提交人: ${env.git_commit_name}    
构建次数：${env.BUILD_NUMBER}    
console output：${env.BUILD_URL}    
                """    
             }    
        }    
    }    
```    
    
---    
    
## 从此自动构建 再也不用盯着构建任务是否结束再通知下游工作人员啦    
    
---    
    
![](..\images\7485616-572b2ff56021dbbd.jpg)    
    
![](..\images\7485616-29af03aa10a901a0.gif)    
