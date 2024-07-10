// OrderProcessor.java
public class OrderProcessor {
    private final Database database;
    private final EmailService emailService;
    private final InventorySystem inventorySystem;

    public OrderProcessor(Database database, EmailService emailService, InventorySystem inventorySystem) {
        this.database = database;
        this.emailService = emailService;
        this.inventorySystem = inventorySystem;
    }

    public void processOrder(Order order) {
        checkItemsAvailability(order.getItems());
        database.saveOrder(order);
        sendOrderConfirmationEmail(order);
        updateInventory(order.getItems());
        applyDiscountIfLoyalCustomer(order);
    }

    private void checkItemsAvailability(Collection<Item> items) {
        for (Item item : items) {
            if (!inventorySystem.isItemAvailable(item)) {
                throw new ItemNotAvailableException("Item not available in inventory: " + item.getName());
            }
        }
    }

    private void sendOrderConfirmationEmail(Order order) {
        String message = "Your order has been received and is being processed.";
        emailService.sendEmail(order.getCustomerEmail(), "Order Confirmation", message);
    }

    private void updateInventory(Collection<Item> items) {
        for (Item item : items) {
            inventorySystem.updateInventory(item, item.getQuantity() * -1);
        }
    }

    private void applyDiscountIfLoyalCustomer(Order order) {
        if (order instanceof LoyalCustomerOrder) {
            LoyalCustomerOrder loyalCustomerOrder = (LoyalCustomerOrder) order;
            loyalCustomerOrder.applyDiscount();
        }
    }
}

public class LoyalCustomerOrder extends Order {
    @Override
    public void applyDiscount() {
        setTotalPrice(getTotalPrice() * 0.9);
    }
}

public class ItemNotAvailableException extends RuntimeException {
    public ItemNotAvailableException(String message) {
        super(message);
    }
}
