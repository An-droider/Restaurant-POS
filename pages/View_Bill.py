
import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize the cart and total price in session state for demonstration purposes
if "cart" not in st.session_state:
    st.write ('Please put items in the cart!')
if "totalprice" not in st.session_state:
    st.write ('Please put items in the cart!')
    

# Function to display and generate the bill
def generate_bill():

    
    if not st.session_state.cart:
        st.write("No items in the cart. Please add items before proceeding.")
        st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Menu.py")
        return
    
    st.title("Payment Successful 🎉")
    st.success("Your order number is {} and will be delivered shortly!".format(st.session_state['order_number']) )
    st.subheader("Your Bill")
    # Bill generation timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"**Generated On:** {timestamp}")
    st.write("Order Number: ",st.session_state['order_number'])



    # Display bill details
    bill_data = []
    for item in st.session_state.cart:
        bill_data.append({
            "Item": item["name"],
            "Quantity": item["quantity"],
            "Price per Unit (Rs.)": item["price"],
            "Total Price (Rs.)": item["price"] * item["quantity"]
        })
    
    df = pd.DataFrame(bill_data)
    custom_index = [f"{i + 1}" for i in range(len(bill_data))]
    df.index = custom_index
    st.table(df)
    
    
    # Display total price
    total_price = st.session_state.totalprice
    st.write(f"**Total Amount Paid: Rs.{total_price:.2f}**")
    
    
    
    # Button to download the bill
    if st.button("Create Bill"):
        create_pdf_bill(df, total_price, timestamp)
        
    # Clear cart after payment
    if st.button("Back to Menu"):
        st.session_state.cart.clear()
        st.session_state.totalprice = 0
        st.write("Cart cleared. Redirecting to menu...")
        st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Menu.py")

# Function to create and download a PDF bill (requires `fpdf` library)
def create_pdf_bill(df, total_price, timestamp):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Cafe De Flora", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="Where Good Food meets Good Memories", ln=True, align="C")
    pdf.ln(10)
    
    #add user details
    # Add user details
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Order Number: {st.session_state['order_number']}", ln=True)
    pdf.cell(0, 10, txt=f"Name: {st.session_state['username']}", ln=True)
    pdf.cell(0, 10, txt=f"Datetime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)


    # Add table headers
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(60, 10, "Item", border=1, align="C")
    pdf.cell(40, 10, "Quantity", border=1, align="C")
    pdf.cell(50, 10, "Price per Unit (Rs.)", border=1, align="C")
    pdf.cell(50, 10, "Total Price (Rs.)", border=1, align="C")
    pdf.ln(10)
    
    # Add table rows
    pdf.set_font("Arial", size=12)
    for index, row in df.iterrows():
        pdf.cell(60, 10, row["Item"], border=1, align="C")
        pdf.cell(40, 10, str(row["Quantity"]), border=1, align="C")
        pdf.cell(50, 10, f"{row['Price per Unit (Rs.)']:.2f}", border=1, align="C")
        pdf.cell(50, 10, f"{row['Total Price (Rs.)']:.2f}", border=1, align="C")
        pdf.ln(10)
    
    # Add total amount
    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt=f"Total Amount Paid: Rs.{total_price:.2f}", ln=True, align="L")
    
    # Save PDF
    pdf_file = "bill.pdf"
    pdf.output(pdf_file)
    
    # Download link
    with open(pdf_file, "rb") as f:
        pdf_data = f.read()
    st.download_button(
        label="Download Bill PDF",
        data=pdf_data,
        file_name=pdf_file,
        mime="application/pdf",
    )

# Run the bill generation function
if __name__ == "__main__":
    generate_bill()
