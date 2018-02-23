#!/bin/bash

javac "$PWD/WordFrequency.java"
javac "$PWD/WordFrequencyTest.java"
java "WordFrequencyTest" < "$PWD/TestFile.txt"
