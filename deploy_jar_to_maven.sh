# deploy jar to nexus maven third party repository.
mvn deploy:deploy-file -DgroupId=your.group.id -DartifactId=your-artifact-id \
-Dversion=1.0.0 -Dpackaging=jar -Dfile=path_to_your.jar -DrepositoryId=releases \
-Durl=http://local.maven.repo:port/nexus/content/repositories/thirdpartyrelease/