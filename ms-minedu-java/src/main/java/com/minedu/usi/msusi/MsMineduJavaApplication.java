package com.minedu.usi.msusi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
public class MsMineduJavaApplication {

	public static void main(String[] args) {
		SpringApplication.run(MsMineduJavaApplication.class, args);
	}

}
