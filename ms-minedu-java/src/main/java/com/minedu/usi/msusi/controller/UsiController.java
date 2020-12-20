package com.minedu.usi.msusi.controller;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.github.damianwajser.exceptions.impl.badrequest.BadRequestException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.Optional;

@RestController
public class UsiController {

    private static final Logger LOGGER = LoggerFactory.getLogger(UsiController.class);


    private final RestTemplate restTemplate;

    private final AmazonDynamoDB amazonDynamoDBClient;

    public UsiController(RestTemplate restTemplate, AmazonDynamoDB amazonDynamoDBClient) {
        this.restTemplate = restTemplate;
        this.amazonDynamoDBClient = amazonDynamoDBClient;
    }

    @GetMapping("/dynamo-tables")
    public Object getDynamoTables() {
        //using amazon client
        return amazonDynamoDBClient.listTables();
    }

    @GetMapping("/echo")
    public Object test() {
        LOGGER.info("echo in service 0 - echoing");
        amazonDynamoDBClient.listTables();
        return restTemplate.getForObject("https://httpbin.org/get", Object.class);
    }

    @GetMapping("/ex")
    public Object testex() throws BadRequestException {
        throw new BadRequestException("", "{message}", Optional.empty());
    }

}
