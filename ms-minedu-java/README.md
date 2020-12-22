
## Initializer

https://start.spring.io/

![Create app](../resources/images/image12.png "Create app")

## Get it!
### Install
#### Maven

Functionality of this package is contained in Java package `com.github.damianwajser`, and can be used using following Maven dependency:


```xml
<dependencies>
		<dependency>
			<groupId>com.github.spring-data-dynamodb</groupId>
			<artifactId>spring-data-dynamodb</artifactId>
			<version>5.0.3</version>
		</dependency>
		<dependency>
			<groupId>com.amazonaws</groupId>
			<artifactId>aws-java-sdk-dynamodb</artifactId>
			<version>${aws-java-sdk-dynamodb.version}</version>
			<exclusions>
				<exclusion>
					<artifactId>commons-logging</artifactId>
					<groupId>commons-logging</groupId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>com.github.derjust</groupId>
			<artifactId>spring-data-dynamodb</artifactId>
			<version>${spring-data-dynamodb.version}</version>
		</dependency>
		<!--utils-->
		<dependency>
			<groupId>org.modelmapper</groupId>
			<artifactId>modelmapper</artifactId>
			<version>2.3.0</version>
		</dependency>
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<optional>true</optional>
		</dependency>
		<!-- ########################################### TESTS #################################################### -->
		<dependency>
			<groupId>com.amazonaws</groupId>
			<artifactId>DynamoDBLocal</artifactId>
			<version>1.11.86</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>com.almworks.sqlite4java</groupId>
			<artifactId>sqlite4java</artifactId>
			<version>1.0.392</version>
			<scope>test</scope>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-actuator</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<dependency>
			<groupId>com.github.damianwajser</groupId>
			<artifactId>spring-commons</artifactId>
			<version>1.15.6</version>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-redis</artifactId>
		</dependency>

		<!-- TESTS -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>

	</dependencies>
 ```




 ## Usage Create a spring-boot application.
```java
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

```
