# Subtitles2Script
A Simple Java Application to Remove Timestamps from Subtitle Files

## Overview

This application removes timestamps from a file containing subtitles. It takes the timestamped text as input and
returns a formatted string without timestamps.

## Usage Example

Original Subtitle File:
```
"00:02:07,156 ﻿Stop! This is the police! 27
00:02:10,236 --> 00:02:11,496 ﻿Don't move! 28
00:02:13,066 --> 00:02:15,266 ﻿Stop immediately! Stop!"
```

Output Subtitle File:
```
"Stop! This is the police!
Don't move!
Stop immediately! Stop!"
```

## How it Works

1. The application reads the input file line by line.
2. The script scrapes timestamps from the input file and removes them.
3. It then formats the remaining text into a single string.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See LICENSE for more
information.
