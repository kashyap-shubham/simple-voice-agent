def create_call_file(mobile_number):
    call_content = f"""Channel: SIP/provider/91{mobile_number}
    Context: outgoing
    Extension: 1000
    Priority: 1
    CallerID: "Recruiter" <1000>
    """
    file_path = f"/var/spool/asterisk/outgoing/call_{mobile_number}.call"
    
    with open(file_path, 'w') as f:
        f.write(call_content)

    import os
    os.chmod(file_path, 0o666)

if __name__ == "__main__":
    number = input("Enter mobile number: ")
    create_call_file(number)
