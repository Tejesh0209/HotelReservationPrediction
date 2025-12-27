pipeline{
    agent any

    stages{
        stage("cloning repo"){
            steps{
                script{
                    echo "cloning repo"
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub-token', url: 'https://github.com/Tejesh0209/HotelReservationPrediction.git']])
                }
    }
}