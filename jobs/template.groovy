// Jenkins job DSL template
pipelineJob('python-pipeline-job') {
    definition {
        cps {
            script(readFileFromWorkspace('Jenkinsfile'))
            sandbox()
        }
    }
    
    triggers {
        scm('H/5 * * * *')  // Poll SCM every 5 minutes
    }
    
    properties {
        disableConcurrentBuilds()
    }
}