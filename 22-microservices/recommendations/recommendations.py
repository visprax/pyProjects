import grpc
import random
from concurrent import futures

import recommendations_pb2_grpc
from recommendations_pb2 import BookCategory, BookRecommendation, RecommendationResponse

books_by_category = {
        BookCategory.MYSTERY: [
            BookRecommendation(id=1, title="Mystery Book 1"),
            BookRecommendation(id=2, title="Mystery Book Two"),
            BookRecommendation(id=3, title="Mystery Book 3"),
            ],
        BookCategory.SCI_FI: [
            BookRecommendation(id=4, title="Sci-Fi Boook 4"),
            BookRecommendation(id=5, title="Sci-Fi Boook Five"),
            BookRecommendation(id=6, title="Sci-Fi Boook Six"),
            ],
        BookCategory.SELF_HELP: [
            BookRecommendation(id=7, title="Don't Read Self-Help!"),
            ]
        }

class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found!")

        book_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        book_to_recommend = random.sample(books_for_category,  num_results)

        return RecommendationResponse(recommendations=books_to_recommend)

