<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = strip_tags(trim($_POST["name"] ?? ""));
  $email = filter_var(trim($_POST["email"] ?? ""), FILTER_SANITIZE_EMAIL);
  $message = trim($_POST["message"] ?? "");

  if (
    empty($name) || 
    empty($message) || 
    !filter_var($email, FILTER_VALIDATE_EMAIL)
  ) {
    http_response_code(400);
    echo json_encode(["success" => false, "message" => "Invalid input. Please fill the form correctly."]);
    exit;
  }

  $to = "growth@meskith.com";
  $subject = "New Contact Form Message from $name";
  $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";
  $headers = "From: $name <$email>";

  if (mail($to, $subject, $body, $headers)) {
    http_response_code(200);
    echo json_encode(["success" => true, "message" => "Message sent successfully!"]);
  } else {
    http_response_code(500);
    echo json_encode(["success" => false, "message" => "Oops! Something went wrong."]);
  }
} else {
  http_response_code(405);
  echo json_encode(["success" => false, "message" => "Method not allowed."]);
}
