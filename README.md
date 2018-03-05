# MakeMessagesPlus

Extend the django makemessages command to make it better

## Installation

Install this repository as a django app inside your django project.

For example use git submodules to clone this repo ( or your fork of it ) inside your django project
seev [the test project](https://github.com/PeteCoward/MakeMessagesPlusTestProject)

Or just clone and copy the code into an app in your project.

## Features

- default to using `--no-location` to simplify diff, turn off by using `--yes-location`
- default to using `--no-wrap` to simplify diff , turn off by using `--yes-wrap`
- allow passing an app list parameter to reduce diffs in apps which have not changed

## Contributing

This is early days, a few more improvements are planned, and more suggestions are welcome.

See the [issue list](https://github.com/PeteCoward/MakeMessagesPlus/issues/)
