/** send html enabled mail via smtp server. */
import java.util.Properties;

import javax.mail.Message;
import javax.mail.Message.RecipientType;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SmtpMailManager {

    private String host = "smtp.office365.com";
    private String port = "587";
    private String fromEmail = "shibli";
    private String password = "******";

    public SmtpMailManager() {
    }

    public SmtpMailManager(String host) {
        this.host = host;
    }

    public SmtpMailManager(String host, String port, String from, String password) {
        this.host = host;
        this.port = port;
        this.fromEmail = from;
        this.password = password;
    }

    public void sendmail(String commaSeparatedEmails, String subject, String body, RecipientType recipientType) {
        Properties props = new Properties();

        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", this.host);
        props.put("mail.smtp.port", this.port);
        props.put("mail.transport.protocol", "smtp");
        props.put("mail.smtp.ssl.trust", this.host);

        // Get the Session object.
        Session session = Session.getInstance(props,
                new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(fromEmail, password);
            }
        });

        try {
            // Create a default MimeMessage object.
            Message message = new MimeMessage(session);
            message.setHeader("Content-type", "text/HTML; charset=UTF-8");
            // Set From: header field of the header.
            message.setFrom(new InternetAddress(fromEmail));
            // Set To/Cc/Bcc: header field of the header.
            message.setRecipients(recipientType, InternetAddress.parse(commaSeparatedEmails));
            // Set Subject: header field
            message.setSubject(subject);
            // Now set the actual message
//            message.setText(body);
            message.setContent(body, "text/html; charset=UTF-8");
            // Send message
            Transport.send(message);
            System.out.println("Sent message successfully....");
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }

    }
}