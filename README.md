# Playwright UI Regression Report

This project is a UI automation regression testing portfolio project built with Python, Pytest, and Playwright.

It demonstrates a black-box UI regression testing workflow for login functionality, including parameterized test cases, Page Object Model structure, automatic failure screenshots, Playwright trace recording, and HTML test report generation.

## Project Purpose

The goal of this project is not only to verify whether UI test cases pass, but also to build a maintainable QA automation workflow.

When a test fails, the framework automatically captures evidence such as screenshots and trace files, allowing QA engineers to review the failure without manually watching the entire test execution.

The test cases do not assume which case will fail. Screenshots are triggered automatically by the test framework only when a test fails.

## Tech Stack

| Category | Tool |
|---|---|
| Language | Python |
| Test Framework | Pytest |
| UI Automation | Playwright |
| Report | pytest-html |
| Test Design | Black-box regression testing |
| Pattern | Page Object Model |
| Package Management | uv |
| Version Control | Git |

## Test Target

Test website:

```text
https://www.saucedemo.com/