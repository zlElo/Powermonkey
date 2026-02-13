def generate_ascii_table(headers, rows):
    if not headers or not rows:
        return ""
    
    # Calculate column widths
    col_widths = [len(str(header)) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):  # Only process if column exists in headers
                col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Create separator line
    separator = "+" + "+".join(["-" * (width + 2) for width in col_widths]) + "+"
    
    # Build table
    table_lines = [separator]
    
    # Add headers
    header_line = "|"
    for i, header in enumerate(headers):
        header_line += f" {str(header).ljust(col_widths[i])} |"
    table_lines.append(header_line)
    table_lines.append(separator)
    
    # Add rows
    for row in rows:
        row_line = "|"
        for i, header in enumerate(headers):
            # Get cell value or empty string if row doesn't have this column
            cell = row[i] if i < len(row) else ""
            row_line += f" {str(cell).ljust(col_widths[i])} |"
        table_lines.append(row_line)
    
    table_lines.append(separator)
    
    return "\n".join(table_lines)