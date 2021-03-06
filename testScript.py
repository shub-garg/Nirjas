#!/usr/bin/env python3

import urllib.request
import unittest
import os


def download_files(cwd):

    url = ["https://raw.github.com/apache/thrift/master/lib/c_glib/test/testbinaryprotocol.c",
    "https://raw.github.com/apache/thrift/master/lib/cpp/test/AnnotationTest.cpp",
    "https://raw.github.com/apache/thrift/master/lib/go/test/tests/thrifttest_driver.go",
    "https://raw.github.com/apache/thrift/master/lib/hs/test/JSONSpec.hs",
    "https://github.com/necolas/normalize.css/blob/master/normalize.css",
    "https://raw.github.com/apache/thrift/master/lib/java/test/org/apache/thrift/test/JavaBeansTest.java",
    "https://raw.github.com/apache/thrift/master/lib/js/test/test-async.js",
    "https://raw.github.com/apache/thrift/master/lib/perl/tools/FixupDist.pl",
    "https://raw.github.com/apache/thrift/master/lib/php/test/Fixtures.php",
    "https://raw.github.com/apache/thrift/master/lib/py/test/test_sslsocket.py",
    "https://raw.github.com/apache/thrift/master/lib/rb/benchmark/benchmark.rb",
    "https://raw.github.com/apache/thrift/master/lib/rs/test/src/bin/kitchen_sink_client.rs",
    "https://raw.github.com/apache/thrift/master/lib/swift/Tests/ThriftTests/TFramedTransportTests.swift",
    "https://raw.github.com/deanwampler/programming-scala-book-code-examples/master/src/main/scala-2/progscala3/metaprogramming/Func.scala",
    "https://raw.github.com/janosgyerik/shellscripts/master/bash/find-recent.sh",
    "https://raw.github.com/antoniolg/Bandhook-Kotlin/master/app/build.gradle.kts",
    "https://raw.github.com/avouros/toolset/master/scripts/BarPlotErrorbars.m",
    "https://raw.github.com/r-lib/rlang/master/R/arg.R",
    "https://raw.github.com/ttu/csharp-tutorial/master/csharp-tutorial/13_Parallel.cs",
    "https://raw.github.com/cfjedimaster/HTML-Code-Demos/master/code/forms/10_validation.html"]
    
    directory = os.path.join(cwd, "nirjas/languages/tests/TestFiles")

    if not os.path.isdir(directory):
        print("Downloading test files")
        os.mkdir(directory)
        for i in url:
            list_of = i.split(".")
            ext = [list_of[-1]]
            data = urllib.request.urlopen(i)

            for j in range (len(ext)):
                filename = "textcomment." + ext[j]
                f = open(os.path.join(directory,filename),'w')
                f.write(data.read().decode('utf-8'))
                f.close
                print(".", end="")
        print()

if __name__ == "__main__":
    here = os.path.abspath(os.path.dirname(__file__))
    download_files(here)
    test_loader = unittest.defaultTestLoader
    test_runner = unittest.TextTestRunner()
    test_suite = test_loader.discover('nirjas/languages/tests',
                                      pattern='test_*.py')
    result = test_runner.run(test_suite)
    exit(int(not result.wasSuccessful()))
