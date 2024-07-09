pipeline {  
    agent any  
        stages {  
       	    stage("Python scripting testing") {  
           	    steps {  
                    sh 'DevOps_Testing.py'
              	    echo "Successfully created text file" 
              	    }  
                catch(error)
                {
                    echo "Unsuccessful"
         	    } 
        }
}
