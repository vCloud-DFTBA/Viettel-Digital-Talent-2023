# Stage 1: Build
FROM maven:3.8.1-jdk-8-slim AS build
WORKDIR /app
COPY . /app
RUN mvn clean package -DskipTests

# Stage 2: Runtime
FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY --from=build /app/target/hw1-docker.jar /app
ENTRYPOINT ["java", "-jar", "hw1-docker.jar"]