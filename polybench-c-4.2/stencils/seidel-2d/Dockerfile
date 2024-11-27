FROM ghcr.io/phoenixflame101/polybench@sha256:3a6e91717902dca33dd7d4023b811954b9e2937ea511b703a0da064c5174c5e8
# Remove all files except ./seidel-2d
RUN find . ! -name 'seidel-2d' -type f -exec rm -f {} +
CMD ["./seidel-2d"]
