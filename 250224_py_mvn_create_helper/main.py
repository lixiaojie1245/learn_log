import os
import sys
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()

# 格式化为指定的字符串格式
formatted_date = now.strftime("%y%m%d%H%M")

if len(sys.argv)==1:
    appName = "tmp"+formatted_date
else:
    appName = sys.argv[1]

os.system("mvn archetype:generate -DgroupId=com.example -DartifactId={} -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false ".format(appName))

with open(f"{appName}/pom.xml") as f:
    text_list=list(map(lambda l: l[:-1] ,f.readlines()))[:-1]+"""<build>
<plugins>
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <version>3.4.3</version>
    <configuration>
        <mainClass>com.example.App</mainClass>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>
</plugins>
</build>""".split() + ['</project>']
    
    newText="\n".join(text_list)
    with open(f"{appName}/pom.xml", 'w') as save_to:
        save_to.write(newText)

with open(f"{appName}/run.sh",'a') as run_sh:
    run_sh.write("mvn clean install\n" + 
                f"java -jar target/${appName}*.jar"
    )
