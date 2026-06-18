# Monitoring Plan

## Purpose

This document outlines the monitoring approach for the churn prediction API after deployment.

## Data Drift

Track changes in feature distributions such as recency, frequency, monetary value, ticket count, and web activity.

## Prediction Distribution

Monitor the percentage of customers predicted as churn and compare it with historical patterns.

## Business Outcomes

Track actual churn outcomes and retention campaign performance.

## API Errors

Monitor response times, failed requests, server errors, and endpoint availability.

## Retraining Triggers

Retraining should be considered if:

* Model performance declines significantly.
* Feature distributions change substantially.
* Business processes or customer behavior change.

## Responsible Use

The API should be used to support retention decisions and customer prioritization.

The API output should not be used as the sole basis for denying services, excluding customers, or making fully automated business decisions without human review.
