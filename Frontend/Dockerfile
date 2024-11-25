# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the static HTML files into the Nginx server's root directory
COPY . /usr/share/nginx/html

# Copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for the web server
EXPOSE 80

# Use the default command to run Nginx
CMD ["nginx", "-g", "daemon off;"]
