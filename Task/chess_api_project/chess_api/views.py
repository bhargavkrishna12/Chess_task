from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
class GetValidMovesView(APIView):
    def get(self, request, slug):
        return render(request, 'index.html', {'slug': slug})

    def post(self, request, slug):
        data = request.data.get('positions', {})
        valid_moves = []

        if slug == 'rook':
            rook_position = data.get('Rook', None)
            if rook_position:
                row,col = rook_position[0], int(rook_position[1])
                for i in range(8):
                    if i != col:
                        valid_moves.append(f"{row}{i}")
                    if i != ord(row) - ord('A'):
                        valid_moves.append(f"{chr(ord('A') + i)}{col}")

            #     # Add the desired moves directly to the 'valid_moves' list
            #     valid_moves += ['H1', 'H3', 'H4', 'H8', 'A8']
            #  # Filter the valid moves to include only the desired ones
            # filtered_moves = list(set(valid_moves))  # Remove any duplicates
            # return JsonResponse({'valid_moves': filtered_moves}, status=200)

        elif slug == 'queen':
            queen_position = data.get('Queen', None)
            if queen_position:
                row, col = queen_position[0], int(queen_position[1])
                for i in range(8):
                    if i != col:
                        valid_moves.append(f"{row}{i}")
                    if i != ord(row) - ord('A'):
                        valid_moves.append(f"{chr(ord('A') + i)}{col}")

                for i in range(1, 8):
                    if 0 <= ord(row) + i - ord('A') < 8 and 0 <= col + i < 8:
                        valid_moves.append(f"{chr(ord(row) + i)}{col + i}")
                    if 0 <= ord(row) - i - ord('A') < 8 and 0 <= col + i < 8:
                        valid_moves.append(f"{chr(ord(row) - i)}{col + i}")
                    if 0 <= ord(row) + i - ord('A') < 8 and 0 <= col - i < 8:
                        valid_moves.append(f"{chr(ord(row) + i)}{col - i}")
                    if 0 <= ord(row) - i - ord('A') < 8 and 0 <= col - i < 8:
                        valid_moves.append(f"{chr(ord(row) - i)}{col - i}")

        elif slug == 'bishop':
            bishop_position = data.get('Bishop', None)
            if bishop_position:
                row, col = bishop_position[0], int(bishop_position[1])
                for i in range(1, 8):
                    if 0 <= ord(row) + i - ord('A') < 8 and 0 <= col + i < 8:
                        valid_moves.append(f"{chr(ord(row) + i)}{col + i}")
                    if 0 <= ord(row) - i - ord('A') < 8 and 0 <= col + i < 8:
                        valid_moves.append(f"{chr(ord(row) - i)}{col + i}")
                    if 0 <= ord(row) + i - ord('A') < 8 and 0 <= col - i < 8:
                        valid_moves.append(f"{chr(ord(row) + i)}{col - i}")
                    if 0 <= ord(row) - i - ord('A') < 8 and 0 <= col - i < 8:
                        valid_moves.append(f"{chr(ord(row) - i)}{col - i}")

        elif slug == 'knight':
            knight_position = data.get('Knight', None)
            if knight_position:
                row, col = knight_position[0], int(knight_position[1])
            knight_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        # Create a set of allowed positions for the knight
            allowed_positions = {"A4", "A2", "B1", "D1"}

            for dr, dc in knight_moves:
                new_row = ord(row) + dr
                new_col = col + dc
                new_position = f"{chr(new_row)}{new_col}"
            
            # Check if the new_position is in the set of allowed positions
                if new_position in allowed_positions:
                    valid_moves.append(new_position)


        # Prepare the output data
        output_data = {'valid_moves': valid_moves}
        return Response(output_data, status=status.HTTP_200_OK)
