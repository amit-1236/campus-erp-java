package com.collegeerp.web;

import com.mysql.cj.jdbc.AbandonedConnectionCleanupThread;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Enumeration;

@WebListener
public class AppContextListener implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent sce) {
        // Initialization if needed
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        // Deregister all JDBC drivers
        Enumeration<Driver> drivers = DriverManager.getDrivers();
        while (drivers.hasMoreElements()) {
            Driver driver = drivers.nextElement();
            try {
                DriverManager.deregisterDriver(driver);
                System.out.println("Deregistering JDBC driver: " + driver);
            } catch (SQLException e) {
                System.err.println("Error deregistering JDBC driver: " + driver);
                e.printStackTrace();
            }
        }
        
        // Stop the MySQL AbandonedConnectionCleanupThread
        AbandonedConnectionCleanupThread.checkedShutdown();
    }
}
