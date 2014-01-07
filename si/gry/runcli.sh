#!/bin/sh
java -cp SnortCLI/target/SnortCLI-1.0-SNAPSHOT.jar:SnortEngine/target/engine-1.0-SNAPSHOT.jar:BoardGame/target/BoardGame-1.0-SNAPSHOT.jar:BoardGameEngine/target/BoardGameEngine-1.0-SNAPSHOT.jar put.ai.snort.snortcli.App $*
