pipeline {
agent any
stages {
stage('Debug: System') {
steps {
echo 'DEBUG: running on node'
// shell may not be available; try uname and fallback
sh 'uname -a || echo NOT-UNIX'
sh 'which sh || echo NO-SH'
}
}
stage('Debug: Workspace') {
steps {
echo 'DEBUG: workspace listing'
sh 'pwd || true'
sh 'ls -la || true'
echo 'DEBUG: Jenkinsfile used by this build (first 200 lines)'
sh 'sed -n "1,200p" Jenkinsfile || true'
}
}
stage('Echo test') {
steps {
echo 'ECHO: Jenkins echo works'
sh 'echo "SH: hello from sh" || true'
}
}
}
}
