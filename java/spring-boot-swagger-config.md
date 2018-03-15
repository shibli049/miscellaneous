# Spring: Spring Cloud

## Description

This is the summary of the linkedin learning course: [Spring: Spring Cloud](https://www.linkedin.com/learning/spring-spring-cloud).

## Add swagger2 documentation

### Dependencies

1. io.springfox:springfox-swagger2:2.4.0
2. io.springfox:springfox-swagger-ui:2.4.0

### Configuration

```java
    @Bean
    public Docket api(){
        return new Docket(DocumentationType.SWAGGER_2)
            .groupName("Room")
            .select()
            .apis(RequestHandlerSelectors.basePackage("com.shibli049.services.room"))
            .paths(any())
            .build()
            .apiInfo(
                new ApiInfo("Room Services",
                    "A set of services to provide data access to rooms",
                    "1.0.0",
                    null,
                    new Contact("Ahmed Shibli", "https://twitter.com/shibli049", null),
                    null, null));
    }
```

And add `@EnableSwagger2` on any `@Configuration` or `Main` class.
