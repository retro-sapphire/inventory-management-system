-- Create USERS table
CREATE TABLE USERS
(
    userId           INT AUTO_INCREMENT PRIMARY KEY,
    name             VARCHAR(255) UNIQUE NOT NULL,
    email            VARCHAR(255) UNIQUE NOT NULL,
    shipping_address VARCHAR(255)        NOT NULL,
    createdAt        DATETIME            NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modifiedAt       DATETIME            NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create INVENTORY table
CREATE TABLE INVENTORY
(
    itemId     INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(255) UNIQUE NOT NULL,
    price      INT                 NOT NULL,
    quantity   INT                 NOT NULL,
    createdAt  DATETIME            NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modifiedAt DATETIME            NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create ORDERS table
CREATE TABLE ORDERS
(
    orderId    INT AUTO_INCREMENT PRIMARY KEY,
    userId     INT      NOT NULL,
    createdAt  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modifiedAt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES USERS (userId)
);

-- Create ORDER_PRODUCTS table
CREATE TABLE ORDER_PRODUCTS
(
    orderId  INT NOT NULL,
    itemId   INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (orderId) REFERENCES ORDERS (orderId),
    FOREIGN KEY (itemId) REFERENCES INVENTORY (itemId)
);

-- insert
INSERT INTO INVENTORY (name, price, quantity)
VALUES ("Apples", 10, 100),
       ("Mangoes", 20, 50),
       ("Oranges", 30, 20),
       ("Kiwi", 40, 100);

INSERT INTO USERS (name, email, shipping_address)
VALUES ("Person A", "persona@example.com", "House A, Sample Country"),
       ("Person B", "personb@example.com", "House B, Sample Country"),
       ("Person C", "personc@example.com", "House C, Sample Country");