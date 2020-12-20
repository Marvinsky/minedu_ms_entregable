package com.minedu.usi.msusi;

import com.minedu.usi.msusi.repository.TeacherObjectRepository;
import org.socialsignin.spring.data.dynamodb.repository.config.EnableDynamoDBRepositories;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

@SpringBootApplication
@EnableDynamoDBRepositories(
		includeFilters = {
				@ComponentScan.Filter(
						type = FilterType.ASSIGNABLE_TYPE,
						classes = {TeacherObjectRepository.class})
		})
@ComponentScan(basePackages = {"com.github.damianwajser", "com.minedu.usi"})
public class MsMineduJavaApplication {

	public static void main(String[] args) {
		SpringApplication.run(MsMineduJavaApplication.class, args);
	}

}
