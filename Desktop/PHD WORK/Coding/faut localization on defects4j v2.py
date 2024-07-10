# invoke_script.py
import subprocess

init_command=[]
work_dir="/home/aiyaya50"
init_command.append ('work_dir="/home/aiyaya50/"')
#setting Gzoltar
init_command.append('export _JAVA_OPTIONS="-Xmx6144M -XX:MaxHeapSize=4096M"&&export MAVEN_OPTS="-Xmx1024M"&&export ANT_OPTS="-Xmx6144M -XX:MaxHeapSize=4096M"')
init_command.append('export GZOLTAR_AGENT_JAR="$work_dir/gzoltar/com.gzoltar.agent.rt/target/com.gzoltar.agent.rt-1.7.4-SNAPSHOT-all.jar"&&\
               export GZOLTAR_CLI_JAR="$work_dir/gzoltar/com.gzoltar.cli/target/com.gzoltar.cli-1.7.4-SNAPSHOT-jar-with-dependencies.jar"')
#initial D4J
# Get D4J
init_command.append('export D4J_HOME="$work_dir/defects4j"&&export TZ="America/Los_Angeles"&&export LC_ALL=en_US.UTF-8 &&export LANG=en_US.UTF-8&&$ export LANGUAGE=en_US.UTF-8')
for cm in init_command:
      process=subprocess.run(cm, shell=True)
      print(process)               
# Command to run the second script

path= 'C:\\Users\\psxai4\\APRs\\FL'
pathR= 'C:\\Users\\psxai4\\APRs\\FL\\Result'
project = ["Closure","Time", "Chart", "Lang", "Math", "Mockito"]
versions=[174, 26, 26, 64, 106, 38]
for i,a in enumerate(project):
    for n in range(1,versions[i]+1, 1):
        command = f"python main.py {path} {pathR} {a} {n} mlp DeepFL softmax 20 10"
        process = subprocess.run(command, shell=True)
        if process.returncode == 0:
            print(f"The {a}-{n} ran successfully.")
        else:
            print("There was an error running {a}-{n}.")
command = f'python rank_parser.py {path} {pathR} DeepFL mlp softmax 20'


# Checkout Closure-27, compile it, and get its metadata
trial= {'Chart':26, 'Time':26,'Collections':4}
v1 = {'Chart':26, 'Time':26, 'Lang':64, 'Mockito':38, 'Math':106, 'JxPath':22,'Closure':174}
v2={'Collections':4, 'Codec':18, 'Csv':16, 'Cli':39, 'Math':106, 'JxPath':22, \
          'Jsoup':93, 'JacksonXml':6,'JacksonDatabind':112, 'JacksonCore':26, 'Gson':18, 'Compress':47, 'Closure':174}
for p in trial:
    PID=p
    BID=v1(p)
    commands=f'cd "{work_dir}"&&rm -rf "{PID}-{BID}b";&&defects4j checkout -p {PID} -v {BID}b -w {PID}-{BID}b'
    command+=f'&&cd {work_dir}/{PID}-{BID}b&&defects4j compile'
    command+='&&test_classpath=$(defects4j export -p cp.test)'
    command+=f'&&src_classes_dir=$(defects4j export -p dir.bin.classes)&&\
    src_classes_dir="{work_dir}/{PID}-{BID}b/$src_classes_dir" \
        &&test_classes_dir=$(defects4j export -p dir.bin.tests)\
            &&test_classes_dir="{work_dir}/{PID}-${BID}b/$test_classes_dir" '
    process = subprocess.run(command, shell=True)
    print(process)
    with open(f"classpath.txt", "a") as f:
        print(f'$test_classpath" >&2', file=f)
        f.close
    with open(f"bin.txt", "a") as s:
        print(f'$src_classes_dir" >&2', file=s)
        s.close
    with open(f"test_bin.txt", "a") as z:
            print(f'{test_class_dir}" >&2', file=z)
            z.close
    command=f'cd "{work_dir}/{PID}-{BID}b"&&unit_tests_file="{work_dir}/{PID}-{BID}b/unit_tests.txt"\
        &&relevant_tests="*"&&'
    # Note, you might want to consider the set of relevant tests provided by D4J, i.e., $D4J_HOME/framework/projects/$PID/relevant_tests/$BID
    command+= f'''java -cp "$test_classpath:$test_classes_dir:$D4J_HOME/framework/projects/lib/junit-4.11.jar:$GZOLTAR_CLI_JAR" \
  com.gzoltar.cli.Main listTestMethods \
    "$test_classes_dir" \
    --outputFile "$unit_tests_file" \
    --includes "$relevant_tests" &&head "$unit_tests_file"'''
    process = subprocess.run(command, shell=True)
    print(process)

    command='''cd "{work_dir}/{PID}-{BID}b"
    &&loaded_classes_file="$D4J_HOME/framework/projects/{PID}/loaded_classes/{BID}.src"
    &&normal_classes=$(cat "$loaded_classes_file" | sed 's/$/:/' | sed ':a;N;$!ba;s/\n//g')
    &&inner_classes=$(cat "$loaded_classes_file" | sed 's/$/$*:/' | sed ':a;N;$!ba;s/\n//g')
    &&classes_to_debug="$normal_classes$inner_classes"
    &&echo "Likely faulty classes: $classes_to_debug" >&2 &&'''
    command+='''cd "{work_dir}/{PID}-${BID}b"
    &&ser_file="{work_dir}/{PID}-{BID}b/gzoltar.ser"
    &&java -XX:MaxPermSize=4096M -javaagent:$GZOLTAR_AGENT_JAR=destfile=$ser_file,buildlocation=$src_classes_dir,includes=$classes_to_debug,excludes="",inclnolocationclasses=false,output="FILE" \
    -cp "$src_classes_dir:$D4J_HOME/framework/projects/lib/junit-4.11.jar:$test_classpath:$GZOLTAR_CLI_JAR" \
    com.gzoltar.cli.Main runTestMethods \
        --testMethods "$unit_tests_file" \
        --collectCoverage'''
    process = subprocess.run(command, shell=True)
    print(process)
    '''
    # Generate fault localization report
    $ cd "$work_dir/$PID-${BID}b"
    $ java -cp "$src_classes_dir:$D4J_HOME/framework/projects/lib/junit-4.11.jar:$test_classpath:$GZOLTAR_CLI_JAR" \
        com.gzoltar.cli.Main faultLocalizationReport \
        --buildLocation "$src_classes_dir" \
        --granularity "line" \
        --inclPublicMethods \
        --inclStaticConstructors \
        --inclDeprecatedMethods \
        --dataFile "$ser_file" \
        --outputDirectory "$work_dir/$PID-${BID}b" \
        --family "sfl" \
        --formula "ochiai" \
        --metric "entropy" \
        --formatter "txt"
    '''''