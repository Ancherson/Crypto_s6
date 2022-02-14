if [ ! -d class ]; then 
    mkdir class
fi

javac -d class Main.java

java -cp class Main $1